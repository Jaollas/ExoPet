from fastapi import APIRouter
from models.animal import Animal
from services.animal_service import adicionar_animal, listar_animais, obter_animal_por_id

router = APIRouter(prefix="/animais", tags=["Animais"])

@router.post("/")
def criar_animal(animal: Animal):
    adicionar_animal(animal)
    return {"message": "Animal cadastrado com sucesso!"}

@router.get("/")
def obter_animais():
    return listar_animais()

from fastapi import HTTPException

@router.get("/{animal_id}")
def obter_animal(animal_id: int):
    animal = obter_animal_por_id(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal
