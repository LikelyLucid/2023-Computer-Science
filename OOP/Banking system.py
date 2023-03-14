class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        # TO COMPLETE
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Street Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"CC Number: {self.cc_number}")
        print(f"CC Type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account Number: {self.account_no}")
        print("##############################################################")

def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8].strip("$")), line[9])

def findUser():
    # TO COMPLETE
    first_name = input("Enter the first name of the user: ").title()
    last_name = input("Enter the last name of the user: ").title()
    for user in userList:
        if user.last_name == last_name and user.first_name == first_name:
            user.displayInfo()
            return user
    print("User not found")

def overdrafts():
    # TO COMPLETE
    num = 0
    balance = int(0)
    for user in userList:
        if user.balance < 0:
            print(f"{user.first_name} {user.last_name}")
            num += 1
            balance += user.balance
    print(f"Total number of users with overdraft accounts: {num}")
    print(f"Total amount of overdraft by all these users: {balance}")

def missingEmails():
    # TO COMPLETE
    num = 0
    for user in userList:
        if user.email == "":
            print(f"{user.first_name} {user.last_name}")
            num += 1
    print(f"Total number of users with missing emails: {num}")

def bankDetails():  # sourcery skip: avoid-builtin-shadow
    print("Total number of users: ", len(userList))
    print("Bank total worth: ", sum(user.balance for user in userList))
    max = userList[0]
    for user in userList:
        if user.balance > max.balance:
            max = user
    print(f"User that has the highest balance: {max.first_name} {max.last_name}, Balance: {max.balance}")
    min = userList[0]
    for user in userList:
        if user.balance < min.balance:
            min = user
    print(f"User that has the lowest balance: {min.first_name} {min.last_name}, Balance: {min.balance}")


def transfer():
    # TO COMPLETE

    True

userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()