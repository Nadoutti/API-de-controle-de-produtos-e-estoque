from fastapi import  FastAPI
from .routers import produtos
from fastapi.middleware.cors import CORSMiddleware
from database.session import create_db_and_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# aqui incluo os routers
app.include_router(produtos.router)

# iniciando o startup


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


