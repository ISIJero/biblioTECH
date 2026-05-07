from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.init_db import create_db
from routers import book, member

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen (importante para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Permite cualquier encabezado
)


@app.on_event("startup")
def startup_event():
    create_db()


app.include_router(book.router, prefix="/books")
app.include_router(member.router, prefix="/members")


@app.get("/test")
def read_root():
    return {"status": "Conectado", "proyecto": "Biblioteca"}
