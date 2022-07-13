from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(book):
    sql = """
    INSERT INTO books (title, genre, fiction, author_id) VALUES (%s, %s, %s, %s) RETURNING *
    """
    values = [book.title, book.genre, book.fiction, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book