# ExoPet

Marketplace básico para animais exóticos (CRUD de usuários e animais) desenvolvido em **Python (FastAPI)** + **SQLite** + **HTML/CSS/JS (Bootstrap)**.  
Projeto criado como portfólio para praticar organização, boas práticas e documentação.

---

## Funcionalidades

- Cadastro de usuários (nome, email, senha)  
- Cadastro de animais (nome, espécie, preço, descrição, dono)  
- Listagem pública de animais disponíveis  
- Visualização dos detalhes de um animal  
- (Opcional) Edição/remoção de anúncios pelo dono  

---

## Tecnologias (Stacks)

**Backend**  
- Python 3  
- FastAPI  
- SQLite  
- Uvicorn (servidor local)  

**Frontend**  
- HTML5  
- CSS3  
- JavaScript  
- Bootstrap (responsividade e estilização)  

**Outros**  
- Git + GitHub (controle de versão)  
- Markdown (documentação)  

---

## Estrutura de Pastas

ExoPet/
│
├── Backend/
│   ├── models/        # Modelos (Usuário, Animal)
│   ├── services/      # Lógica de negócio
│   ├── routes/        # Rotas da API
│   └── main.py        # Arquivo principal do FastAPI
│
├── Frontend/
│   ├── css/           # Estilos
│   ├── js/            # Scripts
│   └── index.html     # Página inicial
│
├── README.md          # Documentação
├── .gitignore         # Arquivos ignorados pelo Git
└── LICENSE            # Licença do projeto

## Como Executar
### Pré-requisitos

- Python 3.9+ instalado
- Git instalado

### Passos

- Clone este repositório:
  git clone https://github.com/Jaollas/ExoPet.git
  cd ExoPet

- Crie e ative um ambiente virtual (opcional, mas recomendado):
  python -m venv venv
  venv\Scripts\activate   # Windows
  source venv/bin/activate   # Linux/Mac

- Instale as dependências:
  pip install fastapi uvicorn

- Inicie o servidor:
  uvicorn Backend.main:app --reload

- Acesse a aplicação:
  API: http://127.0.0.1:8000
  Documentação automática (Swagger UI): http://127.0.0.1:8000/docs
