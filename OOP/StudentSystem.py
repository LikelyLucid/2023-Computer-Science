class Student:
    def __init__(self, name, age, phone_number, formclass, subjects, is_male, enrolled):
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

def print_student_details():
    for student in student_list:
        student.display_info()

student_list = []
Student("Karen", 17, "123-4567", "WNLR", ("13DTC", "13SMX"), False)
Student("Bob", 18, "021-0263674", "BNNL", ("13SMX", "13ENG"), True)
Student("Lisa", 16, "022-4567123", "SKWR", ("13DTC", "13CMX"), False)
Student("Patrick", 18, "023-01234567", "SCBE", ("13ENG", "13CMX", "13DTC"), True)