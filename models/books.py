from flask import Blueprint
from . import db

books_blueprint = Blueprint('books', __name__)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    book_type = db.Column(db.Integer, nullable=False)

    def __init__(self, name, author, year_published, book_type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
    
    @classmethod
    def create_book(cls, name, author, year_published, book_type):
        book = cls(name=name, author=author, year_published=year_published, book_type=book_type)
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def get_books(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls, book_id):
        return cls.query.get(book_id)

    def update(self, name, author, year_published, book_type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        db.session.commit()

    @classmethod
    def delete_book(cls, book_id):
        book = cls.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return True
        return False