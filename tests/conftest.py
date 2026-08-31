import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app as fastapi_app, get_db
from app.utils import gerar_hash
from app.database import Base
from app import models

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool,
                       )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def cliente(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    fastapi_app.dependency_overrides[get_db] = override_get_db

    with TestClient(fastapi_app) as test_client:
        yield test_client

    fastapi_app.dependency_overrides.clear()

@pytest.fixture
def headers_usuario_comum(cliente, db_session):
    user = models.User(
        nome="User comum",
        email="dev@teste.com",
        senha=gerar_hash("123456"),
        is_admin=False
    )
    db_session.add(user)
    db_session.commit()

    res = cliente.post("/login", data={"username": "dev@teste.com", "password": "123456"})
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def headers_admin(cliente, db_session):
    user = models.User(
        nome="User comum",
        email="dev@teste.com",
        senha=gerar_hash("123456"),
        is_admin=True
    )
    db_session.add(user)
    db_session.commit()
    
    res = cliente.post("/login", data={"username": "dev@teste.com", "password": "123456"})
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def servico_valido(db_session):
    novo_servico = models.Servico(
        nome="corte de cabelo",
        preco=50.0,
        ativo=True
    )
    db_session.add(novo_servico)
    db_session.commit()
    db_session.refresh(novo_servico)
    return novo_servico