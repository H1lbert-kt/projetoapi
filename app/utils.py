from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import bcrypt
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha: str):
    pwd_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(pwd_bytes, salt)
    return hash_bytes.decode('utf-8')

def verificar_senha(senha_plana: str, senha_hasheada: str):
    return bcrypt.checkpw(
        senha_plana.encode('utf-8'), 
        senha_hasheada.encode('utf-8')
    )


def criar_token_acesso(id_usuario):
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados = {"user_id": id_usuario,
             "exp": data_expiracao}
    jwt_codificado = jwt.encode(dados, SECRET_KEY, ALGORITHM)
    return jwt_codificado

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        return user_id
    except (JWTError, AttributeError):
        return None