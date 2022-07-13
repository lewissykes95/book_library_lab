from flask import Flask, render_template, Blueprint, request, redirect
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
from models.book import Book

books_blueprint = Blueprint('books', __name__)
