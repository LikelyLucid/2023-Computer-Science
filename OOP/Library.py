class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()  # string with capitalised first letter
        self.author = author  # string
        self.dewey = dewey  # string
        self.isbn = isbn  # string
        self.available = True
        self.borrower = None
        book_list.append(self)

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("##############################################################")


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees: ", self.fees)
        print("##############################################################")


def add_book():
    book_name = input("Enter the title of the book: ").title()
    book_author = input("Enter the author of the book: ").title()
    book_dewey = input("Enter the Dewey number of the book: ").upper()
    book_isbn = input("Enter the ISBN number of the book: ")
    Book(book_name, book_author, book_dewey, book_isbn)
    print(book_name, " has been added")


def add_user():
    name = input("Enter name: ").title()
    address = input("Enter address: ")
    User(name, address)
    print(name, address, "has been added to the system")


def find_book():
    book_to_find = input("Enter the title of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"the book '{book_to_find}' is available")
            return book
    print("Book not found")
    # find_book()


def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print("Hi:", user_to_find)
            return user
        print("User not found")
        return None


def print_info():
    for book in book_list:
        book.book_details()


def print_users():
    for user in user_list:
        user.user_details()


def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.available:
            confirm = input("Are you sure you want to lend this book? (y/n)").lower()
            if confirm == "y":
                print(f"Book Title : {book.title} is now on loan to {user.name}")
                book.available = False
                book.borrower = user.name
                user.borrowed_books.append(book)
        else:
            print("Sorry, this book is not available")


def return_book():
    if user := find_user():
        book = find_book()
        if book.borrower == user.name:
            confirm = input("Are you sure you want to return this book? (y/n)").lower()
            if confirm == "y":
                print(f"Book Title : {book.title} is now available")
                book.borrower = None
                book.available = True
                user.borrowed_books.remove(book)
        else:
            print("Sorry, this book is not available")


book_list = []
user_list = []


Book("Lord of the Rings", "J. R. R. Tolkien", "TOL", "082409640")
Book("The Hunger Games", "Suzanne Collins", "COL", "095395267")
Book("A Tale Of Two Cities", "Charles Dickens", "DIK", "60462809248")
Book("Harry Potter And The Sorcerer's Stone", "J. K. Rowling", "ROW", "9781461245678")

User("John Doe", "123 Fake Street")
User("Jane Doe", "12 Fake Street")
User("Spiderman", "128 Fake Street")

new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")
    action = input("What would you like to do?: ")
    if action == "1":
        lend_book()
    elif action == "2":
        return_book()
    elif action == "3":
        add_user()
    elif action == "4":
        add_book()
    elif action == "5":
        new_action = False
    else:
        print("\nInvalid choice\n")
