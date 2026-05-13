from sqlalchemy import ForeignKey, Integer, DateTime, String, Boolean, Column, Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, index=True, nullable=False)
    senha = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    dono =  relationship("User")
    servico_id = Column(Integer, ForeignKey("servicos.id"))
    servico = relationship("Servico")
    preco_pago = Column(Float, nullable=False)
    status = Column(String, nullable=True, default="confirmado")


class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)