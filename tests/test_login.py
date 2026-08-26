import pytest

def test_login_com_sucesso(cliente):

    payload_usuario = {
        "nome": "devsenior",
        "email": "dev@teste.com",
        "senha": "senhasegura123"
    }
    cliente.post("/usuarios", json=payload_usuario)

    payload_login = {
        "username": "dev@teste.com",
        "password": "senhasegura123"
    }
    response = cliente.post("/login", data=payload_login)

    assert response.status_code == 200
    dados = response.json()
    assert "access_token" in dados
    assert dados["token_type"] == "Bearer"

def test_login_sem_sucesso(cliente):

    payload_usuario = {
        "nome": "devsenior",
        "email": "dev@teste.com",
        "senha": "senhasegura123"
    }
    cliente.post("/usuarios", json=payload_usuario)

    payload_login = {
        "username": "dev@teste.com",
        "password": "senhaerrada123"
    }
    response = cliente.post("/login", data=payload_login)

    assert response.status_code == 401
    assert "Email ou senha inválidos." in response.json()["detail"]

def test_login_usuario_inexistente(cliente):
    payload_login = {
            "username": "dev@teste.com",
            "password": "senhaerrada123"
        }
    response = cliente.post("/login", data=payload_login)

    assert response.status_code == 401
    assert "Email ou senha incorretos" in response.json()["detail"]

