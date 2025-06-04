from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario

SECRET_KEY = "chave_super_segura"
ALGORITHM = "HS256"
EXPIRA_MINUTOS = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def gerar_hash(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha_plain, senha_hashed):
    return pwd_context.verify(senha_plain, senha_hashed)

def criar_token(dados: dict, expires_delta: int = EXPIRA_MINUTOS):
    to_encode = dados.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise Exception()
    except:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user

def get_current_admin(user: Usuario = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Apenas administradores")
    return user
