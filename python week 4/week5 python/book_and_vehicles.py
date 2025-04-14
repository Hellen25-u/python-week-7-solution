# Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# Example usage of Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book1.book_info())  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925

# Vehicle class (Base Class)
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class (Inheriting from Vehicle)
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane class (Inheriting from Vehicle)
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Animal class (Base Class)
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Dog class (Inheriting from Animal)
class Dog(Animal):
    def move(self):
        return "Running 🐕"

# Bird class (Inheriting from Animal)
class Bird(Animal):
    def move(self):
        return "Flying 🦅"

# Creating instances of the vehicles
car = Car()
plane = Plane()

# Creating instances of the animals
dog = Dog()
bird = Bird()

# List of all objects
objects = [car, plane, dog, bird]

# Loop through and call the move() method for each object
for obj in objects:
    print(obj.move())
