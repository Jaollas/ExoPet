from fastapi import FastAPI
from routes import animal_routes, usuario_routes
from services.usuario_service import criar_tabela_usuarios
from services.animal_service import criar_tabela_animais

app = FastAPI(title="ExoPet API")

criar_tabela_usuarios()
criar_tabela_animais()

app.include_router(usuario_routes.router)
app.include_router(animal_routes.router)
