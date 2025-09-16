from fastapi import APIRouter
from models.usuario import Usuario
from services.usuario_service import adicionar_usuario, listar_usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/")
def criar_usuario(usuario: Usuario):
    adicionar_usuario(usuario)
    return {"message": "Usuário cadastrado com sucesso!"}

@router.get("/")
def obter_usuarios():
    return listar_usuarios()
