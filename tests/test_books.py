from fastapi.testclient import TestClient
from bookstore.main import app
from bookstore.core.dependencies import verify_token

# Override JWT dependency
app.dependency_overrides[verify_token] = lambda: {"sub": "test-user"}

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "BookStore API running"
    }


def test_get_books():
    response = client.get("/api/v1/books/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_book():
    payload = {
        "title": "Python Clean Code",
        "author": "Jesus",
        "price": 350.50
    }

    response = client.post(
        "/api/v1/books/",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]

def test_get_book_by_id():
    payload = {
        "title": "FastAPI Expert",
        "author": "Axity",
        "price": 499
    }

    created = client.post("/api/v1/books/", json=payload)
    book_id = created.json()["id"]

    response = client.get(f"/api/v1/books/{book_id}")

    assert response.status_code == 200
    assert response.json()["id"] == book_id


def test_book_not_found():
    response = client.get("/api/v1/books/99999")

    assert response.status_code == 404