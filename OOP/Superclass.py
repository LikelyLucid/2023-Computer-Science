class worker:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job
    def __str__(self):
        return f"{self.name} {self.age} {self.id} {self.birthdate} {self.job}"
class managment(worker):
    def __init__(self, name, age, id, birthdate, job, salary, bonus):
        super().__init__(name, age, id, birthdate, job)
        self.salary = salary
        self.bonus = bonus
    def __str__(self):
        return f"{self.name} {self.age} {self.id} {self.birthdate} {self.job} {self.salary} {self.bonus}"