import pytest
from bookstore.infraestructure.repositories.inmemory_book_repository import (
    InMemoryBookRepository,
)
from bookstore.application.services.book_service import BookService


@pytest.fixture
def book_service():
    repo = InMemoryBookRepository()
    return BookService(repo)