import pytest
from datetime import timedelta, datetime, timezone

def test_criar_agendamento_valido(cliente, headers_usuario_comum, servico_valido):
    data_futura = datetime.now(timezone.utc) + timedelta(days=1)
    data_agendamento = data_futura.replace(hour=10, minute=0, second=0, microsecond=0)

    payload = {
        "servico_id": servico_valido.id,
        "data": data_agendamento.isoformat()
    }

    response = cliente.post("/agendamentos/", json=payload, headers=headers_usuario_comum)

    assert response.status_code == 200
    dados = response.json()
    assert dados["servico_id"] == servico_valido.id
    assert dados["preco_pago"] == servico_valido.preco
    assert "id" in dados

def test_criar_agendamento_data_passada(cliente, headers_usuario_comum, servico_valido):
    data_passada = datetime.now(timezone.utc) - timedelta(days=1)
    data_agendamento = data_passada.replace(hour=10, minute=0, second=0, microsecond=0)
    
    payload = {
        "servico_id": servico_valido.id,
        "data": data_agendamento.isoformat()
    }
    
    response = cliente.post("/agendamentos/", json=payload, headers=headers_usuario_comum)

    assert response.status_code == 400
    assert "A data do agendamento não pode ser no passado." in response.json()["detail"]

def test_criar_agendamento_fora_do_horario_comercial(cliente, headers_usuario_comum, servico_valido):
    data_futura = datetime.now(timezone.utc) + timedelta(days=1)
    data_agendamento = data_futura.replace(hour=22, minute=0, second=0, microsecond=0)
        
    payload = {
        "servico_id": servico_valido.id,
        "data": data_agendamento.isoformat()
    }
        
    response = cliente.post("/agendamentos/", json=payload, headers=headers_usuario_comum)

    assert response.status_code == 400
    assert "Fora do horário comercial (08:00 às 20:00)." in response.json()["detail"]

def test_criar_conflito_no_horario_falha(cliente, headers_admin, headers_usuario_comum, servico_valido):
    data_futura = datetime.now(timezone.utc) + timedelta(days=1)
    data_agendamento = data_futura.replace(hour=14, minute=0, second=0, microsecond=0)
            
    payload = {
        "servico_id": servico_valido.id,
        "data": data_agendamento.isoformat()
    }
            
    res1 = cliente.post("/agendamentos/", json=payload, headers=headers_usuario_comum)
    assert res1.status_code == 200

    res2 = cliente.post("/agendamentos/", json=payload, headers=headers_admin)

    assert res2.status_code == 400
    assert "Este horário já está reservado." in res2.json()["detail"]

def test_dono_cancela_seu_proprio_agendamento(cliente, headers_usuario_comum, servico_valido):
    data_futura = datetime.now(timezone.utc) + timedelta(days=1)
    payload = {
        "servico_id": servico_valido.id,
        "data": data_futura.replace(hour=14, minute=0, second=0, microsecond=0).isoformat()
    }
    res_agendamento = cliente.post("/agendamentos/", json=payload, headers=headers_usuario_comum)
    assert res_agendamento.status_code == 200
    
    agendamento_id = res_agendamento.json()["id"]

    res_cancelar = cliente.post(
        f"/agendamento/cancelar/{agendamento_id}",
        headers=headers_usuario_comum
    )

    assert res_cancelar.status_code == 200
    dados_resposta = res_cancelar.json()
    assert dados_resposta["id"] == agendamento_id