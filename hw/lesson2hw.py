class Worker:
    def __init__(self, name):
        self.name = name
    
    def work(self):
        print(f"{self.name} is working")


class Developer(Worker):
    def work(self):
        print(f"{self.name} writes code")

class Designer(Worker):
    def work(self):
        print(f"{self.name} creates design")

workers = [
    Developer("Alex"),
    Designer("Kate"),
    Worker("Sam")
]

for worker in workers:
    worker.work()
