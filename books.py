from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    Book(2, "My book 2", "Vidhan", "My second book", 3),
    Book(3, "My book 3", "Pandey", "My third book", 4),
    Book(4, "My book 4", "Pandey", "My fourth book", 4),
    Book(5, "My book 5", "Vidhan", "My fifth book", 5),
    Book(6, "My book 6", "Vidhan", "My sixth book", 5),
]

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

@app.get("/books")
def read_all_books():
    return BOOKS

@app.post("/create-book")
def create_book(request_body: BookRequest):
    book = Book(**request_body.model_dump())
    BOOKS.append(book)