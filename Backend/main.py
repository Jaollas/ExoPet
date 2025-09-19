from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import animal_routes, usuario_routes
from services.usuario_service import criar_tabela_usuarios
from services.animal_service import criar_tabela_animais

app = FastAPI(title="ExoPet API")

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

criar_tabela_usuarios()
criar_tabela_animais()

app.include_router(usuario_routes.router)
app.include_router(animal_routes.router)
