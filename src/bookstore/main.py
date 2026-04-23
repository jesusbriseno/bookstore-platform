from fastapi import FastAPI
from bookstore.api.v1.books import router as books_router
from bookstore.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BookStore Platform API",
    version="1.0.0",
    description="API profesional para gestión de libros",
)

app.include_router(books_router)


@app.get("/")
def root():
    return {"message": "BookStore API running"}