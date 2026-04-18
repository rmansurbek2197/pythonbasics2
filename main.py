class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        self.books.append(Book(title, author, "available"))

    def add_user(self, name, email):
        self.users.append(User(name, email))

    def borrow_book(self, user_email, book_title):
        user = next((u for u in self.users if u.email == user_email), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book and book.status == "available":
            user.borrowed_books.append(book)
            book.status = "borrowed"
        else:
            print("Kitobga ega bo'lmaysiz")

    def release_book(self, user_email, book_title):
        user = next((u for u in self.users if u.email == user_email), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book and book.status == "borrowed":
            user.borrowed_books.remove(book)
            book.status = "available"
        else:
            print("Kitobni qaytarib bo'lmaydi")

    def print_borrowed_books(self, user_email):
        user = next((u for u in self.users if u.email == user_email), None)
        if user:
            print([b.title for b in user.borrowed_books])
        else:
            print("Foydalanuvchi topilmadi")

lib = Library()
lib.add_book("Adabiyot", "Xalilullo")
lib.add_book("Tarix", "Shokir")
lib.add_user("Jaloliddin", "jaloliddin@email.com")
lib.borrow_book("jaloliddin@email.com", "Adabiyot")
lib.print_borrowed_books("jaloliddin@email.com")
lib.release_book("jaloliddin@email.com", "Adabiyot")
lib.print_borrowed_books("jaloliddin@email.com")