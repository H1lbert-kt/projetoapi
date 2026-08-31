from dotenv import load_dotenv
import os
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


ph = PasswordHasher()

def gerar_hash(senha: str):
    return ph.hash(senha)

def verificar_senha(senha_plana: str, senha_hasheada: str):
   try:
       return ph.verify(senha_hasheada, senha_plana)
   
   except VerifyMismatchError:
       return False



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