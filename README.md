# Barbearia API

Uma API REST para gerenciamento de agendamentos de barbearia, desenvolvida com FastAPI e focada em boas práticas de segurança, isolamento de ambiente e persistência de dados.

O projeto foi construído de forma autoral, priorizando soluções modernas do mercado backend.

---

## Diferenciais Técnicos do Projeto

* **Segurança com Argon2id:** Utilização do algoritmo Argon2id (vencedor do Password Hashing Competition e recomendado pela OWASP) para criptografia de senhas, garantindo alta proteção contra ataques de força bruta.
* **Infraestrutura com Docker Compose:** Ambiente totalmente orquestrado em containers. A API e o banco de dados rodam de forma isolada, facilitando a execução do projeto em qualquer máquina sem necessidade de configurações locais.
* **Banco de dados Relacional (PostgreSQL):** Utilização de um banco de dados relacional de nível de produção, com persistência de dados utilizando volumes do Docker.
* **Variáveis de Ambiente (.env):** Isolamento completo de credenciais sensíveis (chaves JWT e senhas do banco) utilizando a interpolação nativa no Docker Compose.

---

## Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI** (Framework web de alta performance)
* **SQLAlchemy** (ORM para mapeamento do banco de dados)
* **PostgreSQL** (Banco de dados relacional)
* **Argon2-cffi** (Hash de senhas)
* **PyJWT / Python-Jose** (Autenticação baseada em tokens JWT)
* **Docker & Docker Compose** (Containerização)

---

## Como Rodar o Projeto

É necessário ter o Docker e o Docker Compose instalados na máquina.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/H1lbert-kt/projetoapi.git](https://github.com/H1lbert-kt/projetoapi.git)
cd projetoapi

2. Configurar o arquivo .env

Crie um arquivo chamado .env na raiz do projeto e adicione as seguintes configurações (substitua pelos seus valores reais):
Snippet de código

SECRET_KEY=sua_chave_secreta_para_o_jwt_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
POSTGRES_PASSWORD=sua_senha_segura_do_postgres

3. Subir os Containers

Execute o comando no terminal para construir a imagem da API e iniciar o banco de dados:
Bash

docker-compose up --build

O Docker irá:

    Baixar a imagem do PostgreSQL e iniciar o banco na porta interna padrão.

    Compilar a imagem da API, instalando todas as dependências do arquivo requirements.txt.

    Conectar a API ao banco e rodar a criação automática das tabelas.

Documentação da API (Swagger)

Assim que o container estiver ativo, a documentação interativa completa da API poderá ser acessada pelo navegador para testar a criação de usuários, login com JWT e agendamentos:

    URL das Rotas: http://localhost:8001/docs

Estrutura do Código

O backend foi modularizado para garantir legibilidade e manutenção simplificada:

    database.py: Configuração dinâmica do Engine (identifica automaticamente se roda localmente com SQLite ou via container com PostgreSQL).

    utils.py: Lógica de segurança (regras de expiração do JWT e validação de senhas com Argon2).

    schemas.py: Validação de dados de entrada e saída utilizando Pydantic.