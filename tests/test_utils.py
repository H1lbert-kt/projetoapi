import pytest
from datetime import timedelta, datetime, timezone
from app.utils import gerar_hash, verificar_senha, criar_token_acesso, verificar_token, SECRET_KEY, ALGORITHM
from jose import jwt

def test_gerar_hash_e_verificar_senha_sucesso():
    senha_plana = "minhasenha123"

    senha_hasheada = gerar_hash(senha_plana)

    assert senha_hasheada != senha_plana
    assert verificar_senha(senha_plana, senha_hasheada) is True

def test_gerar_senha_errada():
    senha_correta = "minhasenha123"
    senha_errada = "senhaerrada"

    senha_hasheada = gerar_hash(senha_correta)
    assert verificar_senha(senha_errada, senha_hasheada) is False

def test_criar_e_verificar_token_sucesso():
    user_id = 42

    token = criar_token_acesso(id_usuario=user_id)
    assert isinstance(token, str)

    resuldado_id = verificar_token(token)
    assert resuldado_id == user_id

def test_verificar_token_invalido():
    token_falso = "token.totalmente.invalido123"

    resultado = verificar_token(token_falso)
    assert resultado is None

def test_verificar_token_expirado():
    data_passada = datetime.now(timezone.utc) - timedelta(minutes=10)
    payload_expirado = {
        "user_id": 99,
        "exp": data_passada
    }

    token_expirado = jwt.encode(payload_expirado, SECRET_KEY, algorithm=ALGORITHM)
    resultado = verificar_token(token_expirado)
    assert resultado is None
