<div align="center">

# Barbearia API

### Sistema de agendamentos de barbearia feito com FastAPI, SQLAlchemy e Docker

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

</div>

---

## Sobre o projeto

<<<<<<< HEAD
API REST para gerenciar agendamentos de barbearia. Permite cadastro de usuários, autenticação via JWT, catálogo de serviços com CRUD e agendamentos com validações de horário, conflitos e permissões.
=======
Esse projeto nasceu da necessidade de criar uma API REST moderna e segura para gerenciar agendamentos de barbearia. Aqui você encontra cadastro de usuários, autenticação via JWT, catálogo de serviços com CRUD completo e agendamentos com validações inteligentes (horário comercial, conflitos de agenda, etc.).

Tudo pensado para ser **fácil de rodar** (um único comando Docker) e **seguro de verdade** (Argon2id para senhas, controle de acesso por roles).
>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02

---

## Funcionalidades

<<<<<<< HEAD
- **Autenticação JWT** — Login com tokens de expiração configurável
- **Controle de acesso** — Dois níveis: usuários comuns e administradores
- **CRUD de serviços** — Administradores criam e desativam serviços (soft-delete)
- **Agendamento inteligente** — Valida horário comercial (08h-20h), impede passado e detecta conflitos
- **Cancelamento seguro** — Somente o dono ou um admin pode cancelar
- **Preço congelado** — Valor registrado no momento do agendamento
=======
- **Autenticação JWT** — Login seguro com tokens de expiração configurável
- **Controle de acesso** — Usuários comuns e administradores com permissões distintas
- **CRUD de serviços** — Administradores podem criar e desativar serviços
- **Agendamento inteligente** — Valida horário comercial (08h às 20h), impede agendamentos no passado e detecta conflitos de horário
- **Cancelamento seguro** — Somente o dono do agendamento ou um admin pode cancelar
- **Soft-delete** — Serviços são desativados, não removidos do banco
>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02

---

## Stack utilizada

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.11 |
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Banco de dados | PostgreSQL 15 (Docker) / SQLite (local) |
<<<<<<< HEAD
| Senhas | Argon2id |
=======
| Senhas | Argon2id (OWASP-recommended) |
>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02
| Autenticação | JWT via python-jose |
| Validação | Pydantic v2 |
| Containerização | Docker + Docker Compose |
| Testes | pytest + pytest-cov |

---

## Estrutura do projeto

```
projetoapi/
├── app/
<<<<<<< HEAD
│   ├── __init__.py          # Pacote da aplicação
│   ├── main.py              # Rotas, dependências e instância do FastAPI
│   ├── database.py          # Engine SQLAlchemy e sessão do banco
│   ├── models.py            # Modelos ORM (User, Servico, Agendamento)
│   ├── schemas.py           # Schemas Pydantic para request/response
│   └── utils.py             # Hash de senhas (Argon2id) e JWT
├── tests/
│   ├── __init__.py          # Pacote de testes
│   ├── conftest.py          # Fixtures (banco em memória, clientes HTTP, auth)
│   ├── test_rotas.py        # Testes de criação de usuário
│   ├── test_login.py        # Testes de autenticação
│   ├── test_servicos.py     # Testes de serviços e permissões
│   ├── test_agendamentos.py # Testes de agendamento e validações
│   ├── test_utils.py        # Testes de hash de senhas e JWT
│   └── test_usuarios.py     # (vazio — placeholder)
├── dockerfile               # Build da imagem Python
├── docker-compose.yml       # Orchestration: PostgreSQL + API
├── requirements.txt         # Dependências Python
├── .env.example             # Template de variáveis de ambiente
└── .gitignore
=======
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
>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02
```

---

## Como rodar

### Pré-requisitos

<<<<<<< HEAD
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/)
=======
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/) instalados
>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02

### 1. Clone o repositório

```bash
git clone https://github.com/H1lbert-kt/projetoapi.git
cd projetoapi
```

### 2. Configure as variáveis de ambiente

<<<<<<< HEAD
```bash
cp .env.example .env
```

=======
Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02
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

<<<<<<< HEAD
---

## Variáveis de ambiente

| Variável | Descrição | Default |
|----------|-----------|---------|
| `SECRET_KEY` | Chave secreta para assinar tokens JWT | — |
| `ALGORITHM` | Algoritmo de assinatura JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token (minutos) | `30` |
| `DATABASE_URL` | URL de conexão com o banco | `sqlite:///./banco.db` |
| `POSTGRES_PASSWORD` | Senha do PostgreSQL (usado no Docker) | — |

---

## Endpoints

### Autenticação

| Método | Rota | Autenticação | Descrição |
|--------|------|:------------:|-----------|
| `POST` | `/usuarios/` | Não | Criar novo usuário |
| `POST` | `/login` | Não | Login e retorno do token JWT |

### Administração

| Método | Rota | Autenticação | Descrição |
|--------|------|:------------:|-----------|
| `GET` | `/usuarios/listar/` | Admin | Listar todos os usuários |
| `POST` | `/servicos/` | Admin | Criar novo serviço |
| `DELETE` | `/servicos/{id}` | Admin | Desativar serviço |

### Operações

| Método | Rota | Autenticação | Descrição |
|--------|------|:------------:|-----------|
| `GET` | `/servicos/listar_ativos/` | Não | Listar serviços ativos |
| `POST` | `/agendamentos/` | Usuário | Criar agendamento |
| `POST` | `/agendamentos/cancelar/{id}` | Usuário | Cancelar agendamento |
| `GET` | `/agendamentos/meus/` | Usuário | Listar meus agendamentos |

---

## Modelos de dados

### User

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer | Identificador único (autoincremento) |
| `nome` | String | Nome do usuário |
| `email` | String | Email (único, indexado) |
| `is_admin` | Boolean | Perfil administrador (default: `false`) |

### Servico

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer | Identificador único (autoincremento) |
| `nome` | String | Nome do serviço |
| `preco` | Float | Preço do serviço |
| `ativo` | Boolean | Status ativo (default: `true`) |

### Agendamento

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer | Identificador único (autoincremento) |
| `data` | DateTime | Data e hora do agendamento (UTC) |
| `usuario_id` | Integer | FK → User |
| `servico_id` | Integer | FK → Servico |
| `preco_pago` | Float | Preço congelado no momento do agendamento |
| `status` | String | `confirmado` ou `cancelado` |

---

## Regras de negócio

- **Horário comercial:** Agendamentos somente entre 08h e 20h (UTC)
- **Sem agendamento no passado:** Data e hora devem ser futuras
- **Serviço ativo obrigatório:** Serviços desativados não podem ser agendados
- **Sem conflitos de serviço:** Dois agendamentos no mesmo horário para o mesmo serviço são bloqueados
- **Sem dupla reserva:** Um usuário não pode ter dois agendamentos no mesmo horário
- **Preço congelado:** O valor registrado é o preço do serviço no momento do agendamento
- **Cancelamento restrito:** Somente o dono do agendamento ou um administrador pode cancelar

---

## Segurança

- **Senhas:** Argon2id (recomendado pelo OWASP)
- **Tokens JWT:** Assinatura HS256 com expiração configurável
- **Validação de email:** Formato validado via Pydantic (`EmailStr`)
- **Controle de acesso:** Rotas administrativas protegidas por middleware de role
- **Soft-delete:** Serviços são desativados, não removidos do banco

---

## Testes

### Rodar localmente (sem Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest --cov=app tests/
```

### Estrutura dos testes

| Arquivo | Cobertura |
|---------|-----------|
| `test_rotas.py` | Criação de usuário, email duplicado |
| `test_login.py` | Login com sucesso, senha errada, usuário inexistente |
| `test_servicos.py` | Listar serviços, criar serviço (admin), permissão negada (user) |
| `test_agendamentos.py` | Agendamento válido, data passada, horário comercial, conflito, cancelamento |
| `test_utils.py` | Hash/verificação de senha, criação/verificação de JWT, token expirado |

---

## Como contribuir

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Faça commit (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

<div align="center">

Feito com dedicação por [H1lbert-kt](https://github.com/H1lbert-kt)

=======
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

>>>>>>> da1d5d19bf44e9a04828853f112160f82fe71e02
</div>
