from fastapi import APIRouter, Query
from models.animal import Animal
from services.animal_service import adicionar_animal, listar_animais, obter_animal_por_id, atualizar_animal, deletar_animal

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

@router.get("/")
def obter_animais(dono_id: int | None = Query(default=None)):
    return listar_animais(dono_id)

@router.put("/{animal_id}")
def atualizar_animal_route(animal_id: int, animal: Animal, usuario_id: int):
    sucesso, mensagem = atualizar_animal(animal_id, animal, usuario_id)
    if not sucesso:
        raise HTTPException(status_code=403 if mensagem == "Usuário não autorizado" else 404, detail=mensagem)
    return {"message": mensagem}

@router.delete("/{animal_id}")
def deletar_animal_route(animal_id: int, usuario_id: int):
    sucesso, mensagem = deletar_animal(animal_id, usuario_id)
    if not sucesso:
        raise HTTPException(status_code=403 if mensagem == "Usuário não autorizado" else 404, detail=mensagem)
    return {"message": mensagem}
