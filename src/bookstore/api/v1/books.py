from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from bookstore.db.database import SessionLocal
from bookstore.schemas.book import BookCreate, BookUpdate, Book

from bookstore.application.services.book_service import BookService
from bookstore.infraestructure.repositories.sql_book_repository import (
    SqlBookRepository,
)

router = APIRouter(
    prefix="/api/v1/books",
    tags=["Books"]
)


# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency Service
def get_service(db: Session = Depends(get_db)):
    repo = SqlBookRepository(db)
    return BookService(repo)


# GET ALL
@router.get("/", response_model=list[Book], status_code=200)
def get_books(service: BookService = Depends(get_service)):
    return service.list_books()


# GET BY ID
@router.get("/{book_id}", response_model=Book, status_code=200)
def get_book(book_id: int, service: BookService = Depends(get_service)):
    book = service.get_book(book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# CREATE
@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    data: BookCreate,
    service: BookService = Depends(get_service)
):
    return service.create_book(
        title=data.title,
        author=data.author,
        price=data.price
    )