import pytest

@pytest.fixture
def obter_headers(cliente):
    cliente.post("/usuarios/", json={
        "nome": "user comum", "email": "dev@teste.com", "senha": "123"
    })
    res = cliente.post("/login", data={
        "username": "dev@teste.com",
        "password": "123"
    })
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_listar_servicos_ativos_com_sucesso(cliente, obter_headers):
    response = cliente.get("/servicos/listar_ativos/",
                            headers=obter_headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_criar_agendamento_sem_token_falha(cliente):
    payload_agendamento = {
        "servico_id": 1,
        "data": "2026-09-01T10:00:00Z"
    }

    response = cliente.post("/agendamentos/", json=payload_agendamento)

    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]

def test_criar_agendamento_token_invalido_falha(cliente):
    headers_falsos = {"Authorization": "Bearer token.totalmente.falso"}

    payload_agendamento = {
        "servico_id": 1,
        "data": "2026-09-01T10:00:00Z"
    }

    response = cliente.post("/agendamentos/", json=payload_agendamento, headers=headers_falsos)

    assert response.status_code == 401
    assert response.json()["detail"] == "Token inválido."