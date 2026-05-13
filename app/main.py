from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .utils import gerar_hash, verificar_senha, criar_token_acesso, verificar_token
from . import models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def obter_usuario(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    verificacao = verificar_token(token)
    if verificacao is None:
        raise HTTPException(status_code=401, detail="Token inválido.")
    
    usuario = db.query(models.User).filter(models.User.id == verificacao).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return usuario

def verificar_admin(usuario_atual: models.User = Depends(obter_usuario)):
    if not usuario_atual.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Operação restrita a administradores."
        )
    return usuario_atual

@app.post("/login", tags=["Autenticação"])
def login(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.email == login_data.username).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos.")
    
    senha_valida = verificar_senha(login_data.password, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")
    
    token = criar_token_acesso(usuario.id)
    return {"access_token": token, "token_type": "Bearer"}

@app.post("/usuarios/", tags=["Autenticação"], response_model=schemas.UserOut)
def criar_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    email_existe = db.query(models.User).filter(models.User.email == usuario.email).first()
    if email_existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    
    novo_usuario = models.User(
        nome=usuario.nome, 
        email=usuario.email, 
        senha=gerar_hash(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.get("/usuarios/listar/", tags=["Administração"], response_model=list[schemas.UserOut])
def listar_usuario(db: Session = Depends(get_db), admin = Depends(verificar_admin)):
    usuarios = db.query(models.User).all()
    return usuarios

@app.get("/servicos/listar_ativos/", tags=["Operações"], response_model=list[schemas.ServicoOut])
def listar_servicos_ativos(db: Session = Depends(get_db)):
    servicos = db.query(models.Servico).filter(models.Servico.ativo == True).all()
    return servicos

@app.post("/servicos/", tags=["Administração"], response_model=schemas.ServicoOut)
def criar_servico(servico_criar: schemas.ServicoCreate, db: Session = Depends(get_db), admin = Depends(verificar_admin)):
    servico = db.query(models.Servico).filter(models.Servico.nome == servico_criar.nome).first()
    if servico:
        raise HTTPException(status_code=400, detail="O serviço já existe.")
    
    novo_servico = models.Servico(nome=servico_criar.nome, preco=servico_criar.preco)
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@app.delete("/servicos/{servico_id}", tags=["Administração"])
def deletar_servico(servico_id: int, db: Session = Depends(get_db), admin = Depends(verificar_admin)):
    servico = db.query(models.Servico).filter(models.Servico.id == servico_id).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    
    servico.ativo = False
    db.commit()
    return {"detail": "Serviço desativado com sucesso."}

@app.post("/agendamentos/", tags=["Operações"], response_model=schemas.AgendamentoOut)
def agendamento(
    agendamento_in: schemas.AgendamentoCreate,
    db: Session = Depends(get_db),
    usuario_atual: models.User = Depends(obter_usuario)
):
    if agendamento_in.data < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="A data do agendamento não pode ser no passado.")
    
    if agendamento_in.data.hour >= 21 or agendamento_in.data.hour <= 7:
        raise HTTPException(
            status_code=400,
            detail="Fora do horário comercial (08:00 às 20:00)."
        )

    servico = db.query(models.Servico).filter(
        models.Servico.id == agendamento_in.servico_id,
        models.Servico.ativo == True
    ).first()
    
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    
    conflito = db.query(models.Agendamento).filter(
        models.Agendamento.servico_id == agendamento_in.servico_id,
        models.Agendamento.data == agendamento_in.data
    ).first()
    
    if conflito:
        raise HTTPException(status_code=400, detail="Este horário já está reservado.")
    
    conflito_usuario = db.query(models.Agendamento).filter(
        models.Agendamento.usuario_id == usuario_atual.id,
        models.Agendamento.data == agendamento_in.data,
        models.Agendamento.status == "confirmado"
    ).first()

    if conflito_usuario:
        raise HTTPException(
            status_code=400,
            detail="Você já possui um agendamento neste horário."
        )
    
    novo = models.Agendamento(
        preco_pago=servico.preco,
        servico_id=servico.id,
        data=agendamento_in.data,
        usuario_id=usuario_atual.id
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/agendamento/cancelar/", response_model=schemas.AgendamentoOut, tags=["Operações"])
def cancelar_agendamento(agendameto_id: int, db: Session = Depends(get_db), usuario_atual = Depends(obter_usuario)):
    buscar_agendamento = db.query(models.Agendamento).filter(models.Agendamento.id == agendameto_id).first()
    if not buscar_agendamento:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )
    
    if usuario_atual.id != buscar_agendamento.usuario_id and not usuario_atual.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para realizar este processo."
        )
    
    if buscar_agendamento.status == "cancelado":
        raise HTTPException(
            status_code=400,
            detail="O agendamento já está cancelado."
        )

    buscar_agendamento.status = "cancelado"
    db.commit()
    db.refresh(buscar_agendamento)
    return buscar_agendamento

@app.get("/agendamentos/meus/", tags=["Operações"], response_model=list[schemas.AgendamentoOut])
def meus_agendamentos(usuario_atual: models.User = Depends(obter_usuario), db: Session = Depends(get_db)):
    agendamento_meus = db.query(models.Agendamento).filter(
        models.Agendamento.usuario_id == usuario_atual.id,
          models.Agendamento.status == "confirmado"
          ).order_by(models.Agendamento.data.asc()).all()
    return agendamento_meus
