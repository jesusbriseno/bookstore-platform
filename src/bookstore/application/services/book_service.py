from bookstore.domain.entities.book import BookEntity
from bookstore.ports.repositories.book_repository import BookRepository


class BookService:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def list_books(self):
        return self.repository.get_all()

    def get_book(self, book_id: int):
        return self.repository.get_by_id(book_id)

    def create_book(self, title: str, author: str, price: float):
        book = BookEntity(
            id=None,
            title=title,
            author=author,
            price=price
        )

        return self.repository.create(book)