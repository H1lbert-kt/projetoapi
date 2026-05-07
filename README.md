Status do Projeto
Este sistema encontra-se em fase de desenvolvimento ativo. A arquitetura atual estabelece a base fundamental de segurança e agendamento, estando previstas futuras atualizações para maximizar as funcionalidades de gestão e relatórios.

Projeto API de Agendamento

Este repositório contém uma interface de programação de aplicações (API) desenvolvida para a gestão de agendamentos de serviços. O sistema foi concebido utilizando o framework FastAPI, priorizando a performance, a validação de dados e a segurança das operações.

Visão Geral

A solução permite o gerenciamento completo de fluxos de trabalho, incluindo o cadastro de usuários, a definição de serviços disponíveis e a reserva de horários. A aplicação implementa regras de negócio que impedem agendamentos duplicados no mesmo intervalo e bloqueia registros em datas retroativas.

Tecnologias Utilizadas

    Linguagem: Python 3.13

    Framework: FastAPI

    ORM: SQLAlchemy

    Banco de Dados: SQLite

    Segurança: Autenticação JWT e Criptografia Bcrypt

    Validação: Pydantic

Estrutura do Projeto

    app/main.py: Ponto de entrada da aplicação e definição das rotas.

    app/models.py: Mapeamento das tabelas e entidades do banco de dados.

    app/schemas.py: Definição dos contratos de entrada e saída de dados.

    app/database.py: Configuração da infraestrutura de persistência.

    app/utils.py: Lógica auxiliar de segurança e geração de tokens.

Procedimentos de Instalação

    Clonar o Repositório
    git clone https://github.com/H1lbert-kt/projetoapi.git
    cd projetoapi

    Ambiente Virtual
    python -m venv venv
    (Ative o ambiente de acordo com seu sistema operacional)

    Dependências
    pip install -r requirements.txt

    Execução do Servidor
    uvicorn app.main:app --reload

Documentação Interativa

Após iniciar o servidor, a documentação completa dos endpoints, incluindo exemplos de requisição e esquemas de dados, estará disponível no endereço local: http://127.0.0.1:8000/docs
