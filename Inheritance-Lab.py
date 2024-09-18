from animal import Animal
class dog(Animal):
    def brak(self):
        return 'barking'# dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def bark(self):
        return f"{self.name} is barking..."

