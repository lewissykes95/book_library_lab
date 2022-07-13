from flask import Flask, render_template, Blueprint, request, redirect
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.book import Book
from models.author import Author

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def index():
    books = book_repo.select_all()
    return render_template('index.html', all_books = books)

@books_blueprint.route('/books/new')
def new():
    authors = author_repo.select_all()
    return render_template('books/new.html', all_authors = authors)

@books_blueprint.route('/books', methods=['POST'])
def create():
    title = request.form['title']
    genre = request.form['genre']
    fiction = request.form['fiction']
    author = author_repo.select(request.form['author_id'])
    book = Book(title, genre, fiction, author)
    book_repo.save(book)
    return redirect('/books')
