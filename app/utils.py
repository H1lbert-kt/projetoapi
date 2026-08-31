import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from dotenv import load_dotenv
from jose import JWTError, jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("ERRO CRÍTICO: A variável de ambiente 'SECRET_KEY' não está definida!")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

ph = PasswordHasher()

def gerar_hash(senha: str) -> str:
    return ph.hash(senha)

def verificar_senha(senha_plana: str, senha_hasheada: str) -> bool:
    try:
        return ph.verify(senha_hasheada, senha_plana)
    except (VerifyMismatchError, InvalidHashError):
        return False

def criar_token_acesso(id_usuario: int) -> str:
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    dados = {
        "sub": str(id_usuario),
        "exp": data_expiracao
    }
    
    jwt_codificado = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_codificado

def verificar_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: Optional[str] = payload.get("sub")
        return user_id
    except JWTError:
        return None