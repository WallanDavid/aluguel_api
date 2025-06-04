from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Contrato
from schemas import ContratoBase, ContratoOut
from typing import List
from auth import get_current_user

router = APIRouter(prefix="/contratos", tags=["Contratos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ContratoOut)
def criar_contrato(contrato: ContratoBase, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_contrato = Contrato(**contrato.dict())
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

@router.get("/", response_model=List[ContratoOut])
def listar_contratos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Contrato).all()
