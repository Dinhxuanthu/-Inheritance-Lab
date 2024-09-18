

class Animal:
    def eat(self):
        return 'eating'
from animal import Animal
class cat(Animal):
    def meow(self):
        return 'meowing'
from animal import Animal
class Dog(Animal):
    def bark(self):
        return 'barking'
animal=Animal()
print(animal.eat())