class worker:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job
    def __str__(self):
        return f"{self.name} {self.age} {self.id} {self.birthdate} {self.job}"
class managment:
    def __init__(self, workers):
        self.workers = workers
    def add_worker(self, name, age, id, birthdate, job):
        self.workers.append(worker(name, age, id, birthdate, job))
    def print_workers(self):
        for worker in self.workers:
            print(worker)
    def print_workers_by_job(self, job):