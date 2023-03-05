class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title() # string with capitalised first letter
        self.author = author # string
        self.dewey = dewey # string
        self.isbn = isbn # string
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

def add_user

def print_info():
    for book in book_list:
        book.book_details()

def print_users():
    for user in user_list:
        user.user_details()


book_list = []
user_list = []


Book("Lord of the Rings", "J. R. R. Tolkien", "TOL", "082409640")
Book("The Hunger Games", "Suzanne Collins", "COL", "095395267")
Book("A Tale Of Two Cities", "Charles Dickens", "DIK", "60462809248")
Book("Harry Potter And The Sorcerer's Stone", "J. K. Rowling", "ROW", "9781461245678")

User("John Doe", "123 Fake Street")
User("Jane Doe", "12 Fake Street")
User("Spiderman", "128 Fake Street")

print_info()
print_users()