from fastapi import APIRouter
from models.animal import Animal
from services.animal_service import adicionar_animal, listar_animais

router = APIRouter(prefix="/animais", tags=["Animais"])

@router.post("/")
def criar_animal(animal: Animal):
    adicionar_animal(animal)
    return {"message": "Animal cadastrado com sucesso!"}

@router.get("/")
def obter_animais():
    return listar_animais()
