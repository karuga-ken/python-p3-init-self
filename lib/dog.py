#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

dog = Dog("Curtis")
print(dog.name)
print(dog.breed)