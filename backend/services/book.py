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

    return data


def get_book_by_id(id: int) -> Book:
    query = """SELECT * FROM libros WHERE id = :id"""
    data = list()
    with dbm:
        rows = dbm.extract_data(query=query, param={"id": id})

        for row in rows:
            data.append(dict(row))

    return data[0]


def insert_books(book: BookIn) -> Book:
    query = """
    INSERT INTO libros (nombre, autor, materia, isbn, cod, estado) 
    VALUES (:nombre, :autor, :materia, :isbn, :cod, :estado)
    """

    with dbm:
        last_record_id = dbm.execute_query(query=query, param=book.model_dump())
    return {**book.model_dump(), "id": last_record_id.lastrowid}


def update_book_by_id(id: int, book: BookIn) -> Book:
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


def delete_book_by_id(id: int) -> dict:
    query = """DELETE FROM libros WHERE id = :id"""
    param = {"id": id}
    with dbm:
        result = dbm.execute_query(query=query, param=param)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Libro no encontrado")

    return {"Result": "Libro eliminado exitosamente"}
