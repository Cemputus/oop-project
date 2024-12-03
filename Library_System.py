class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available


class Library:
    total_books = 0

    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)
        Library.total_books += copies
        print(f"Added {title} by {author} with {copies} copies.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.copies_available > 0:
                book.copies_available -= 1
                Library.total_books -= 1
                print(f"Borrowed {title}.")
                return
        print(f"{title} is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies_available += 1
                Library.total_books += 1
                print(f"Returned {title}.")
                return
        print(f"{title} is not in the library.")

    def display_library_info(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Copies: {book.copies_available}")


# Demonstration
library = Library()
library.add_book("Python 101", "John Doe", 5)
library.add_book("AI Basics", "Jane Smith", 3)
library.add_book("Data Science", "Alice Johnson", 4)

library.borrow_book("Python 101")
library.return_book("AI Basics")
library.display_library_info()
