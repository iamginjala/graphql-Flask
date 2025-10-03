from flask import Flask
from strawberry.flask.views import GraphQLView
import strawberry

# defining the books data

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]


@strawberry.type
class Book:
    id: int
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def get_books(self):
        return [Book(**book) for book in books]
    
    @strawberry.field
    def get_books_by_id(self,id:int):
        book_data = next((book for book in books if book['id'] == id),None)
        if book_data:
            return Book(**book_data)
        return None
schema = strawberry.Schema(query=Query)

app = Flask(__name__)

