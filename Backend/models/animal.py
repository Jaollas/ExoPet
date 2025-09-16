from pydantic import BaseModel

class Animal(BaseModel):
    id: int | None = None
    nome: str
    especie: str
    descricao: str
    preco: float
    dono_id: int
