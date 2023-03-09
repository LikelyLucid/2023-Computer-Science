student_list = []
class Student:
    def __init__(self, name, age, phone_number, formclass, subjects, is_male, enrolled=True):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.formclass = formclass
        self.subjects = subjects
        self.is_male = True
        self.enrolled = True
        student_list.append(self)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Form Class: {self.formclass}")
        print(f"Subjects: {self.subjects}")
        print(f"Is Male: {self.is_male}")
        print(f"Enrolled: {self.enrolled}")
        print("##############################################################")

def add_student():
    Name = input("Enter Name: ").title()
    age = int(input("Enter Age: "))
    PhoneNumber = input("Enter Phone Number: ")
    Formclass = input("Enter Form Class: ")
    while True:
        subjects = input("Enter Subject\n(Enter 'q' to quit): ").title()
        

def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            is_male = line[5] == "True"
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)

def print_student_details():
    for student in student_list:
        student.display_info()

def find_student():
    student_to_find = input("Enter the name of the student: ").title()
    for student in student_list:
        if student.name == student_to_find:
            student.display_info()
            return student
    print("Student not found")

def select_student_age():
    count = 0
    age = int(input("Enter the age of the students: "))
    for student in student_list:
        if student.age >= age:
            student.display_info()
            count += 1
    print(f"{count} students are older than {age}")

def count_in_class():
    class_name = input("Enter the name of the class: ").upper()
    count = 0
    for student in student_list:
        if student.formclass == class_name:
            count += 1
    print(f"{class_name} has {count} students")

action = True
while action:
    print("#### MENU ####")
    print("(1) Count Students Taking Subject")
    print("(2) Print Full List of students")
    print("(3) Print Students about particular age")
    print("(4) Get details of particular Student")
    print("(5) Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        count_in_class()
    elif choice == "2":
        print_student_details()
    elif choice == "3":
        select_student_age()
    elif choice == "4":
        find_student()
    elif choice == "5":
        action = False
    else:
        print("Invalid choice")


generate_students()
find_student()