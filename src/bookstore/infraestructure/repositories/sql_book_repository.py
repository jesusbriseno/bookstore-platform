from sqlalchemy.orm import Session
from bookstore.models.book import Book
from bookstore.domain.entities.book import BookEntity
#from bookstore.ports.repositories.book_repository import BookRepository
from bookstore.domain.repositories.book_repository import BookRepository


class SqlBookRepository(BookRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[BookEntity]:
        books = self.db.query(Book).all()

        return [
            BookEntity(
                id=b.id,
                title=b.title,
                author=b.author,
                price=b.price
            )
            for b in books
        ]

    def get_by_id(self, book_id: int) -> BookEntity | None:
        book = self.db.query(Book).filter(Book.id == book_id).first()

        if not book:
            return None

        return BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            price=book.price
        )

    def create(self, entity: BookEntity) -> BookEntity:
        book = Book(
            title=entity.title,
            author=entity.author,
            price=entity.price
        )

        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

        return BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            price=book.price
        )