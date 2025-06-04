from fastapi import FastAPI
from database import Base, engine
from routers import usuarios, imoveis, contratos, login

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Aluguel de Imóveis")

app.include_router(usuarios.router)
app.include_router(imoveis.router)
app.include_router(contratos.router)
app.include_router(login.router)
