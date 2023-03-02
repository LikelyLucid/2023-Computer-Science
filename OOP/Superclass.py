class worker:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        self.earnings = 0

    def lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)