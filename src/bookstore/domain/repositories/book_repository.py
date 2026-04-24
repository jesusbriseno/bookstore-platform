from typing import Protocol
from bookstore.domain.entities.book import BookEntity


class BookRepository(Protocol):

    def get_by_id(self, book_id: int) -> BookEntity | None:
        ...

    def get_all(self) -> list[BookEntity]:
        ...

    def create(self, book: BookEntity) -> BookEntity:
        ...