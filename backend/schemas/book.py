from pydantic import BaseModel


class Book(BaseModel):
    id: int
    nombre: str
    autor: str
    materia: str
    isbn: str
    cod: int
    estado: int


class BookIn(BaseModel):
    nombre: str
    autor: str
    materia: str
    isbn: str
    cod: int
    estado: int
