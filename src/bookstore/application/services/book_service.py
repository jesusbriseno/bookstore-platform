from bookstore.domain.entities.book import BookEntity
#from bookstore.ports.repositories.book_repository import BookRepository
from bookstore.core.exceptions import AppException
from bookstore.domain.repositories.book_repository import BookRepository


class BookService:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def list_books(self):
        return self.repository.get_all()

    def get_book(self, book_id: int):
        book = self.repository.get_by_id(book_id)

        if not book:
            raise AppException(
                status_code=404,
                error_code="BOOK_404",
                error_message=f"Book with id {book_id} not found",
                user_error="El libro solicitado no existe",
            )

        return book

    def create_book(self, title: str, author: str, price: float):
        book = BookEntity(
            id=None,
            title=title,
            author=author,
            price=price
        )

        return self.repository.create(book)