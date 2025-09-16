from pydantic import BaseModel

class Usuario(BaseModel):
    id: int | None = None
    nome: str
    email: str
    senha: str
