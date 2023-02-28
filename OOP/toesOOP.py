class Toes:
    def __init__(self, size):
        self.size = size
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < self.size:
            self.count += 1
            return self.count
        else:
            raise StopIteration