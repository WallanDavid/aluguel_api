from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

class Imovel(Base):
    __tablename__ = "imoveis"
    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String, nullable=False)
    descricao = Column(String)
    valor = Column(Integer)

class Contrato(Base):
    __tablename__ = "contratos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    data_inicio = Column(Date)
    data_fim = Column(Date)

    usuario = relationship("Usuario")
    imovel = relationship("Imovel")
