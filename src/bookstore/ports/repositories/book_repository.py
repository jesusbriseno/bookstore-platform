from abc import ABC, abstractmethod
from bookstore.domain.entities.book import BookEntity


class BookRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[BookEntity]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> BookEntity | None:
        pass

    @abstractmethod
    def create(self, book: BookEntity) -> BookEntity:
        pass