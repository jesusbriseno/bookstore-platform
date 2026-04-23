from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    price: float


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)