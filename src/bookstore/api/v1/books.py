from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from bookstore.core.dependencies import verify_token
from bookstore.core.exceptions import AppException
from bookstore.db.database import SessionLocal
from bookstore.schemas.book import BookCreate, BookUpdate, Book

from bookstore.application.services.book_service import BookService


from bookstore.infraestructure.repositories.sql_book_repository import (
    SqlBookRepository,
)

#memory_repo = InMemoryBookRepository()

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

# @router.get("/", response_model=list[Book])
# def get_books(
#     limit: int = 10,
#     offset: int = 0,
#     service: BookService = Depends(get_service)
# ):
#     return service.list_books(limit=limit, offset=offset)

# GET BY ID
@router.get("/{book_id}", response_model=Book, status_code=200)
def get_book(book_id: int, service: BookService = Depends(get_service)):
    book = service.get_book(book_id)

    return book

# CREATE
@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    data: BookCreate,
    service: BookService = Depends(get_service),
    user=Depends(verify_token)
):
    return service.create_book(
        title=data.title,
        author=data.author,
        price=data.price
    )