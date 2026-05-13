Sistema de Agendamento de Serviços (API)

Este projeto consiste em uma API REST desenvolvida com FastAPI para a gestão de agendamentos de serviços. O sistema foi projetado para atender tanto clientes, que podem gerenciar suas próprias reservas, quanto administradores, que possuem controle sobre o catálogo de serviços e a base de usuários.
Principais Funcionalidades

    Autenticação e Segurança: Implementação de fluxo OAuth2 com JWT (JSON Web Tokens) para proteção de rotas.

    Gestão de Serviços: CRUD completo para administração de serviços com suporte a Soft Delete (desativação lógica para preservação de integridade referencial).

    Validações de Agendamento:

        Impedimento de reservas em datas ou horários passados.

        Restrição de funcionamento apenas para horário comercial definido (08:00 às 20:00).

        Verificação dupla de conflitos: impede que um serviço seja reservado por dois clientes no mesmo horário e que um único cliente possua agendamentos simultâneos.

    Controle de Acesso (RBAC): Middleware de dependências para separar permissões de usuários comuns e administradores.

Tecnologias Utilizadas

    Python 3.10+

    FastAPI (Framework Web)

    SQLAlchemy (ORM para persistência de dados)

    Pydantic (Validação de dados e Schemas)

    SQLite (Banco de dados relacional local)

    Passlib (Hashing de senhas com algoritmos seguros)

Estrutura do Projeto

.
├── app/
│   ├── main.py          # Inicialização da API e definição de endpoints
│   ├── models.py        # Mapeamento das tabelas do banco de dados
│   ├── schemas.py       # Modelos de dados para entrada e saída (Pydantic)
│   ├── database.py      # Configuração do motor e sessões do SQLAlchemy
│   └── utils.py         # Lógica de criptografia e geração/verificação de tokens
├── requirements.txt     # Listagem de dependências do ambiente
└── README.md            # Documentação do projeto
Instruções para Execução

    Clonar o repositório:
    git clone https://github.com/H1lbert-kt/projetoapi.git
    cd projetoapi

    Configurar o ambiente virtual:
    python -m venv venv
    No Windows:

    venv\Scripts\activate
    No Linux/Mac:

    source venv/bin/activate

    Instalar as dependências:
    pip install -r requirements.txt

    Iniciar a aplicação:
    uvicorn app.main:app --reload

A documentação Swagger estará disponível em: http://127.0.0.1:8000/docs
Decisões Técnicas

Uma decisão central na arquitetura deste sistema foi a persistência do preço no momento do agendamento (campo preco_pago). Diferente de apenas referenciar o preço atual do serviço, esta abordagem garante a imutabilidade do registro financeiro histórico. Caso o valor de um serviço seja reajustado futuramente, os registros de agendamentos realizados anteriormente não sofrerão alterações indevidas, garantindo relatórios precisos.
