
from enum import Enum


class Book:
    _isbns = []

    def __init__(self):
        self._title = ""
        self._author = ""
        self._isbn = ""
        self._available = True

    def __str__(self):
        return (f"Book\n"
                f"title: {self._title}, "
                f"author: {self._author}, "
                f"isbn: {self._isbn}, "
                f"available: {self._available}")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title: str):
        if new_title and not new_title.isspace():
            self._title = new_title
        else:
            print("Cтрока title, не может быть пустой")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author: str):
        if new_author and not new_author.isspace():
            self._author = new_author
        else:
            print("Cтрока author, не может быть пустой")

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, new_isbn):
        if new_isbn not in self._isbns:
            self._isbn = new_isbn
            self._isbns.append(new_isbn)
        else:
            print("Cтрока isbn, должна быть уникальной для каждой книги")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, new_available):
        if isinstance(new_available, bool):
            self._available = new_available


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, new_book: Book):
        for book in self._books:
            if book.isbn == new_book.isbn:
                print("Книга с таким ISBN существует.")
                return False

        self._books.append(new_book)
        return True

    def remove_book(self, book_isbn):
        for book in self._books:
            if book.isbn == book_isbn:
                self._books.remove(book)
                print("Книга с таким ISBN удалена.")
                return None

        print("Книга с таким ISBN не существует.")

    def find_book_by_title(self, title):
        for book in self._books:
            if book.title == title:
                print(f"Книга {title} найдена.")
                return book
        print(f"Книга {title} не найдена.")

    def find_book_by_author(self, author):
        book_by_author = []
        for book in self._books:
            if book.author == author:
                book_by_author.append(book)
        if book_by_author:
            return book_by_author

    def borrow_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn and book.available is True:
                book.available = False
                return True
        return False

    def return_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn and book.available is False:
                book.available = True
                return True
        return False


class Format(Enum):
    PDF = "pdf"
    EPUB = "epub"


class Ebook(Book):
    def __init__(self):
        super().__init__()
        self._format = Format

    def __str__(self):
        return (f"Ebook\n"
                f"title: {self._title}, "
                f"author: {self._author}, "
                f"isbn: {self._isbn}, "
                f"available: {self._available}, "
                f"format: {self._format}")


b1, b2, b3, eb1 = Book(), Book(), Book(), Ebook()
b1.title = "Shrek"
b1.author = "Pushkin"
b1.isbn = "a"
print(f"isbn: {b1.isbn}")
b2.title = "Shrek 2"
b2.author = "Pushkin"
b2.isbn = "a"
b3.title = "Kolobok"
b3.author = "author2"
b3.isbn = "b"
print(f"isbn: {b2.isbn}")
eb1.title = "Shrek"
eb1.author = "Pushkin"
eb1.isbn = "c"

l1 = Library()
l1.add_book(b1)
l1.remove_book("a")
l1.find_book_by_title("Shrek")
l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
l1.add_book(eb1)
print(l1.find_book_by_author("Pushkin"))
l1.borrow_book("c")
print(eb1)
l1.return_book("c")
print(eb1)
