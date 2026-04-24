import pytest
from bookstore.core.exceptions import AppException
from bookstore.core.dependencies import verify_token

app.dependency_overrides[verify_token] = lambda: {"sub": "test-user"}

def test_get_non_existing_book_raises_exception(book_service):
    with pytest.raises(AppException) as exc:
        book_service.get_book(999)

    assert exc.value.status_code == 404
    assert exc.value.detail["errorCode"] == "BOOK_404"

def test_create_book(book_service):
    book = book_service.create_book(
        title="Clean Architecture",
        author="Robert C. Martin",
        price=450,
    )

    assert book.id == 1
    assert book.title == "Clean Architecture"
    assert book.author == "Robert C. Martin"
    assert book.price == 450


def test_get_book(book_service):
    created = book_service.create_book(
        title="DDD",
        author="Eric Evans",
        price=600,
    )

    found = book_service.get_book(created.id)

    assert found.id == created.id
    assert found.title == "DDD"


def test_list_books(book_service):
    book_service.create_book("Book 1", "Author 1", 100)
    book_service.create_book("Book 2", "Author 2", 200)

    books = book_service.list_books()

    assert len(books) == 2