class Visitor:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = None
        self.next = None

class Book:
    def __init__(self, title):
        self.title = title
        self.next = None

class Library:
    def __init__(self):
        self.visitors = None

    def add_visitor(self, name):
        new_visitor = Visitor(name)
        if self.visitors is None:
            self.visitors = new_visitor
        else:
            current = self.visitors
            while current.next is not None:
                current = current.next
            current.next = new_visitor

    def borrow_book(self, visitor_name, book_title):
        visitor = self.find_visitor(visitor_name)
        if visitor is None:
            print(f"{visitor_name} is not registered as a visitor.")
            return

        new_book = Book(book_title)
        if visitor.borrowed_books is None:
            visitor.borrowed_books = new_book
        else:
            current_book = visitor.borrowed_books
            while current_book.next is not None:
                current_book = current_book.next
            current_book.next = new_book

    def print_books(self, visitor_name):
        visitor = self.find_visitor(visitor_name)
        if visitor is None:
            print(f"{visitor_name} is not registered as a visitor.")
            return

        print(f"Books borrowed by {visitor.name}:")
        current_book = visitor.borrowed_books
        if current_book is None:
            print("No books borrowed.")
        else:
            while current_book is not None:
                print(current_book.title)
                current_book = current_book.next

    def find_visitor(self, visitor_name):
        current = self.visitors
        while current is not None:
            if current.name == visitor_name:
                return current
            current = current.next
        return None

# Contoh penggunaan program
library = Library()

library.add_visitor("Siti")
library.add_visitor("Rina")

library.borrow_book("Siti", "Harry Potter and the Sorcerer's Stone")
library.borrow_book("Siti", "The Great Gatsby")
library.borrow_book("Rina", "To Kill a Mockingbird")

library.print_books("Siti")
print()
library.print_books("Rina")
