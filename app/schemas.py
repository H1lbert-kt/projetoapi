from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):

    nome: str
    email: str
    senha: str

class UserOut(BaseModel):

    id: int
    nome: str
    email: str

    model_config = {"from_attributes": True}

class UserLogin(BaseModel):

    email: str
    senha: str

class AgendamentoCreate(BaseModel):

    servico_id: int
    data: datetime

    model_config = {"from_attributes": True}

class AgendamentoOut(BaseModel):

    id: int
    data: datetime
    usuario_id: int
    servico_id: int
    preco_pago: float

class ServicoCreate(BaseModel):

    nome: str
    preco: float

class ServicoOut(BaseModel):

    id: int
    nome: str
    preco: float
    ativo: bool

    model_config = {"from_attributes": True}