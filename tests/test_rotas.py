import pytest

def test_criar_usuario_com_sucesso(cliente):
    payload = {
        "nome": "devsenior",
        "email": "dev@teste.com",
        "senha": "senhasegura123"
    }

    response = cliente.post("/usuarios", json=payload)

    assert response.status_code == 200

    dados = response.json()
    assert dados["email"] == "dev@teste.com"
    assert "id" in dados
    assert "senha" not in dados

def test_criar_usuario_email_duplicado(cliente):
    payload = {
            "nome": "devsenior",
            "email": "dev@teste.com",
            "senha": "senhasegura123"
        }

    cliente.post("/usuarios", json=payload)
    
    response = cliente.post("/usuarios", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email já cadastrado."