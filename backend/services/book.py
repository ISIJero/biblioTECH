from schemas.book import Book, BookIn
from config.db_connection import DataBaseManagment
from typing import List
from fastapi import HTTPException

dbm = DataBaseManagment()


def get_all_books() -> List[Book]:
    query = """SELECT * FROM libros"""
    data = list()
    with dbm:
        rows = dbm.extract_data(query=query)

        for row in rows:
            data.append(dict(row))

    for datum in data:
        if not datum["estado"]:
            datum["estado"] = "Disponible"
        else:
            datum["estado"] = "Prestado"

    return data


def get_book_by_id(id: int) -> Book:
    query = """SELECT * FROM libros WHERE id = :id"""
    data = list()
    with dbm:
        rows = dbm.extract_data(query=query, param={"id": id})

        for row in rows:
            data.append(dict(row))

    if not data[0]["estado"]:
        data[0]["estado"] = "Disponible"
    else:
        data[0]["estado"] = "Prestado"

    return data[0]


def add_books(book: BookIn) -> Book:
    query = """
    INSERT INTO libros (nombre, autor, materia, isbn, cod, estado) 
    VALUES (:nombre, :autor, :materia, :isbn, :cod, :estado)
    """

    with dbm:
        last_record_id = dbm.execute_query(query=query, param=book.model_dump())
    return {**book.model_dump(), "id": last_record_id.lastrowid}


def update_book(id: int, book: BookIn) -> Book:
    query = """
    UPDATE libros 
    SET nombre = :nombre, 
        autor = :autor, 
        materia = :materia, 
        isbn = :isbn, 
        cod = :cod, 
        estado = :estado 
    WHERE id = :id"""
    param = {**book.model_dump(), "id": id}
    with dbm:
        dbm.execute_query(query=query, param=param)
    return {**book.model_dump(), "id": id}


def delete_book(id: int) -> dict:
    query = """DELETE FROM libros WHERE id = :id"""
    param = {"id": id}
    with dbm:
        result = dbm.execute_query(query=query, param=param)
        if not result.rowcount:
            raise HTTPException(status_code=404, detail="Libro no encontrado")

    return {"Result": "Libro eliminado exitosamente"}


if __name__ == "__main__":

    print(get_book_by_id(1))
