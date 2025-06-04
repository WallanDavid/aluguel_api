from pydantic import BaseModel
from datetime import date
from typing import Optional

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str
    is_admin: Optional[bool] = False

class UsuarioOut(UsuarioBase):
    id: int
    is_admin: bool
    model_config = {"from_attributes": True}

class ImovelBase(BaseModel):
    endereco: str
    descricao: Optional[str]
    valor: int

class ImovelCreate(ImovelBase): pass

class ImovelOut(ImovelBase):
    id: int
    model_config = {"from_attributes": True}

class ContratoBase(BaseModel):
    usuario_id: int
    imovel_id: int
    data_inicio: date
    data_fim: date

class ContratoOut(ContratoBase):
    id: int
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str
