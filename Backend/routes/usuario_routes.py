from fastapi import APIRouter
from models.usuario import Usuario
from services.usuario_service import adicionar_usuario, listar_usuarios, autenticar_usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/")
def criar_usuario(usuario: Usuario):
    adicionar_usuario(usuario)
    return {"message": "Usuário cadastrado com sucesso!"}

@router.get("/")
def obter_usuarios():
    return listar_usuarios()

from fastapi import HTTPException

@router.post("/login")
def login(email: str, senha: str):
    usuario = autenticar_usuario(email, senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "Login realizado com sucesso!", "usuario": usuario}

@router.post("/logout")
def logout():
    return {"message": "Logout realizado com sucesso!"}
