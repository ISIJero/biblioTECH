import services.book as services
from schemas.book import Book, BookIn
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Book])
def read_books():
    return services.get_all_books()


@router.get("/{id}", response_model=Book)
def read_book_by_id(id: int):
    return services.get_book_by_id(id)


@router.post("/", response_model=Book)
def add_book(book: BookIn):
    return services.insert_books(book)


@router.put("/{id}", response_model=Book)
def update_book(id: int, book: BookIn):
    return services.update_book_by_id(id, book)


@router.delete("/{id}")
def delete_book(id: int):
    return services.delete_book_by_id(id)
