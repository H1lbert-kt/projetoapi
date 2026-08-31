<div align="center">

# Barbearia API

### Sistema de agendamentos de barbearia feito com FastAPI, SQLAlchemy e Docker

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#licença)

</div>

---

## Sobre o projeto

Esse projeto nasceu da necessidade de criar uma API REST moderna e segura para gerenciar agendamentos de barbearia. Aqui você encontra cadastro de usuários, autenticação via JWT, catálogo de serviços com CRUD completo e agendamentos com validações inteligentes (horário comercial, conflitos de agenda, etc.).

Tudo pensado para ser **fácil de rodar** (um único comando Docker) e **seguro de verdade** (Argon2id para senhas, controle de acesso por roles).

---

## Funcionalidades

- **Autenticação JWT** — Login seguro com tokens de expiração configurável
- **Controle de acesso** — Usuários comuns e administradores com permissões distintas
- **CRUD de serviços** — Administradores podem criar e desativar serviços
- **Agendamento inteligente** — Valida horário comercial (08h às 20h), impede agendamentos no passado e detecta conflitos de horário
- **Cancelamento seguro** — Somente o dono do agendamento ou um admin pode cancelar
- **Soft-delete** — Serviços são desativados, não removidos do banco

---

## Stack utilizada

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.11 |
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Banco de dados | PostgreSQL 15 (Docker) / SQLite (local) |
| Senhas | Argon2id (OWASP-recommended) |
| Autenticação | JWT via python-jose |
| Validação | Pydantic v2 |
| Containerização | Docker + Docker Compose |
| Testes | pytest + pytest-cov |

---

## Estrutura do projeto

```
projetoapi/
├── app/
│   ├── main.py          # Rotas e configuração da aplicação
│   ├── database.py      # Engine e sessão do banco (SQLite ou PostgreSQL)
│   ├── models.py        # Modelos SQLAlchemy (User, Servico, Agendamento)
│   ├── schemas.py       # Schemas Pydantic para validação
│   └── utils.py         # Utilitários de segurança (hash + JWT)
├── tests/
│   ├── conftest.py      # Fixtures de teste (banco em memória, clientes HTTP)
│   ├── test_rotas.py    # Testes de criação de usuário
│   ├── test_login.py    # Testes de autenticação
│   ├── test_servicos.py # Testes de serviços e permissões
│   ├── test_agendamentos.py # Testes de agendamento e validações
│   └── test_utils.py    # Testes de hash de senhas e JWT
├── dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Como rodar

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/) instalados

### 1. Clone o repositório

```bash
git clone https://github.com/H1lbert-kt/projetoapi.git
cd projetoapi
```

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o `.env` com seus valores:

```env
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
POSTGRES_PASSWORD=sua_senha_segura
DATABASE_URL=postgresql://admin:sua_senha_segura@db:5432/barbearia
```

### 3. Suba os containers

```bash
docker-compose up --build
```

A API estará disponível em: **http://localhost:8001/docs**

> A documentação interativa do Swagger será aberta automaticamente no navegador.

---

## Endpoints

| Método | Rota | Autenticação | Descrição |
|--------|------|:------------:|-----------|
| `POST` | `/usuarios/` | Não | Criar novo usuário |
| `POST` | `/login` | Não | Fazer login e receber token JWT |
| `GET` | `/usuarios/listar/` | Admin | Listar todos os usuários |
| `GET` | `/servicos/listar_ativos/` | Não | Listar serviços ativos |
| `POST` | `/servicos/` | Admin | Criar novo serviço |
| `DELETE` | `/servicos/{id}` | Admin | Desativar serviço |
| `POST` | `/agendamentos/` | Usuário | Criar agendamento |
| `POST` | `/agendamento/cancelar/{id}` | Usuário | Cancelar agendamento |
| `GET` | `/agendamentos/meus/` | Usuário | Listar meus agendamentos |

---

## Regras de negócio

- **Horário comercial:** Agendamentos só entre 08h e 20h
- **Sem agendamento no passado:** Data e hora devem ser futuras
- **Serviço ativo obrigatório:** Só é possível agendar serviços ativos
- **Sem conflitos:** Dois agendamentos no mesmo horário para o mesmo serviço são bloqueados
- **Dupla reserva:** Um usuário não pode ter dois agendamentos no mesmo horário
- **Preço congelado:** O valor pago é registrado no momento do agendamento, não mudando se o preço do serviço for alterado depois

---

## Testes

Para rodar os testes localmente (sem Docker):

```bash
# Crie um venv e instale as dependências
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Execute os testes
pytest --cov=app tests/
```

</div>
