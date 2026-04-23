from dataclasses import dataclass


@dataclass
class BookEntity:
    id: int | None
    title: str
    author: str
    price: float

    def is_expensive(self) -> bool:
        return self.price > 500