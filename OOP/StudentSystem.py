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

def select_student_age():
    age = int(input("Enter the age of the students: "))
    for student in student_list:
        if student.age >= age:
            student.display_info()

def count_in_class():
    class_name = input("Enter the name of the class: ").upper()
    count = 0
    for student in student_list:
        if student.formclass == class_name:
            count += 1
    print(f"{class_name} has {count} students")

student_list = []
generate_students()
count_in_class()