from bookstore.domain.repositories.book_repository import BookRepository
from bookstore.domain.entities.book import BookEntity


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        print("INMEMORY REPO CREATED")
        self._books: dict[int, BookEntity] = {}
        self._id_counter = 1

    def get_by_id(self, book_id: int) -> BookEntity | None:
        return self._books.get(book_id)

    def get_all(self) -> list[BookEntity]:
        return list(self._books.values())

    def create(self, book: BookEntity) -> BookEntity:
        book.id = self._id_counter
        self._books[self._id_counter] = book
        self._id_counter += 1
        return book