from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def save(book):
    sql = """
    INSERT INTO books (title, genre, fiction, author_id) VALUES (%s, %s, %s, %s) RETURNING *
    """
    values = [book.title, book.genre, book.fiction, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books =[]
    sql = """
    SELECT * FROM books ORDER BY id
    """
    results = run_sql(sql)
    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['fiction'], author, row['id'])
        books.append(book)
    return books

def delete_all():
    run_sql("DELETE FROM books")

def delete(id):
    sql = """
    DELETE FROM books WHERE id = %s
    """
    values = [id]
    run_sql(sql, values) 

def select(id):
    book = None
    sql = """
    SELECT * FROM books WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'],result['genre'], result['fiction'], author, result['id'] )
    return book






