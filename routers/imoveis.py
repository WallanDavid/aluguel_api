from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Imovel
from schemas import ImovelCreate, ImovelOut
from typing import List
from auth import get_current_user, get_current_admin

router = APIRouter(prefix="/imoveis", tags=["Imóveis"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ImovelOut)
def criar_imovel(imovel: ImovelCreate, db: Session = Depends(get_db), user=Depends(get_current_admin)):
    db_imovel = Imovel(**imovel.dict())
    db.add(db_imovel)
    db.commit()
    db.refresh(db_imovel)
    return db_imovel

@router.get("/", response_model=List[ImovelOut])
def listar_imoveis(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Imovel).all()
