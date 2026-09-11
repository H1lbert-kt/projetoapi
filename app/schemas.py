from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime, timezone

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UserOut(BaseModel):
    id: int
    nome: str
    email: str

    model_config = {"from_attributes": True}

class AgendamentoCreate(BaseModel):
    servico_id: int
    data: datetime

    @field_validator("data")
    @classmethod
    def garantir_utc(cls, v):
        if v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v

class AgendamentoOut(BaseModel):
    id: int
    data: datetime
    usuario_id: int
    servico_id: int
    preco_pago: float

class ServicoCreate(BaseModel):
    nome: str
    preco: float

class ServicoOut(BaseModel):
    id: int
    nome: str
    preco: float
    ativo: bool

    model_config = {"from_attributes": True}