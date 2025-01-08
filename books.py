from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "My book 1", "Vidhan", "My first book", 5),
    Book(2, "My book 2", "Vidhan", "My first book", 3),
    Book(3, "My book 3", "Pandey", "My first book", 4),
    Book(4, "My book 4", "Pandey", "My first book", 4),
    Book(5, "My book 5", "Vidhan", "My first book", 5),
    Book(6, "My book 6", "Vidhan", "My first book", 5),
]

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

@app.get("/books")
def read_all_books():
    return BOOKS

@app.post("/create-book")
def create_book(request_body: BookRequest):
    book = Book(**request_body.model_dump())
    BOOKS.append(book)