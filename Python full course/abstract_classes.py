# An abstract class is a class which constais one or more abstact methods.
# An abstract method is a method that has a declaration but does not have
# an implementation.

# An abstract class prevents an user from creating an object of that class.
# It compels a user to override abstract methods in a child class.


class Vehicle:

    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")


vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

print("\n--------------------------\n")


# Since the Vehicle class is too generic, I want to prevent an user from
# creating an object from it. I can turn it into an abstract class using
# the "abc" (Abstract Base Class) module:

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


try:
    vehicle = Vehicle()

except TypeError as te:
    print(f"Error: {te}")

print("\n--------------------------\n")


# In my abstract "ABC" class, I need at least one abstract method, otherwise I will
# be able to create objects from it:

class Vehicle(ABC):

    def start(self):
        print("The vehicle is started")


try:
    vehicle = Vehicle()

except TypeError as te:
    print(f"Error: {te}")

else:
    print("Object created!")

print("\n--------------------------\n")


# It will work even this way:

class Vehicle(ABC):
    pass


try:
    vehicle = Vehicle()

except TypeError as te:
    print(f"Error: {te}")

else:
    print("Object created!")

print("\n--------------------------\n")


# I am compelled to override methods in child classes:

class Vehicle2(ABC):

    @abstractmethod
    def go(self):
        pass


class Car2(Vehicle2):

    def go(self):
        print("You drive the car")


class Motorcycle2(Vehicle2):
    pass


car = Car2()

try:
    motorcycle = Motorcycle2()

except TypeError as te:
    print(f"Error: {te}")

else:
    print("correct!")

# To create a Car and Motorcycle class, I need to override the
# abstract methods of the parent class.
