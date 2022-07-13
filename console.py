import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author1 = Author('Roald', 'Dahl')
author2 = Author('Charles', 'Dickens')
author3 = Author('Charlotte', 'Bronte')
author4 = Author('Gay', 'Talese')
author_repo.save(author1)
author_repo.save(author2)
author_repo.save(author3)
author_repo.save(author4)

book1 = Book('James and the Giant Peach', 'Childrens', True, author1)
book2 = Book('Great Expectations', 'Novel', True, author2)
book3 = Book('Jane Eyre', 'Romance', True, author3)
book4 = Book ('The Voyeurs Motel', 'True Crime', False, author4)
book_repo.save(book1)
book_repo.save(book2)
book_repo.save(book3)
book_repo.save(book4)