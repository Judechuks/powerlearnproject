"""
What is Inheritance?
The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
Inheritance promotes code reusability, which is considered one of the best industrial coding practices as it makes the codebase modular.
In inheritance, the child class acquires all the data members, properties, and functions from the parent class. Also, a child class can also provide its specific implementation to the methods of the parent class.

Example: 
In the real world, a Car is a subclass/Child of a Vehicle class(Parent). We can create a Car by inheriting the properties of a Vehicle such as Wheels, Colors, Fuel tank, engine, and add extra properties in Car as required.

Syntax:
class ParentClass:
  # Body of the parent class
class ChildClass(ParentClass):
  # Body of the child class

Types of inheritance in Python
There are 5 different types of inheritance. This is based on the number of child and parent classes involved. 
Let's explore them here:
Single inheritance
Multiple Inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritanc

1. Single Inheritance:
A child class inherits from a single parent class
Example
Let’s create one parent class called Vehicle and one child class called Car to implement single inheritance. 
"""
# Base/Parent class
class Vehicle:
  def vehicle_info(self):
    print("Inside Parent(Vehicle) class")

# child/sub/derived class
class Car(Vehicle):
  def car_info(self):
    print("Inside Child(Car) class")

# create object of car
car = Car()
# access Vehicle's info using car object
car.vehicle_info()
car.car_info()

"""
2. Multiple Inheritance
Here, one Child class inherits from multiple parent classes. It means the child class has access to all the parent classes' methods and attributes.
Example:
Let's create two parent 2 Parent classes Person and Company. Then create a Child class Employee. Which inherits from the two parent classes.
"""
# Parent class 1
class Person:
  def person_info(self, name, age):
    print("Inside Person class")
    print(f"Name: {name} Age: {age}")

# Parent class 2
class Company:
  def company_info(self, company_name, location):
    print("Inside Company class")
    print(f"Name: {company_name} Location: {location}")

# child class
class Employee(Person, Company):
  def employee_info(self, salary, skill):
    print("Inside Car class")
    print(f"Name: {salary} Location: {skill}")

# create object of Employee
emp = Employee()
# access info
emp.person_info("Jessica", 28)
emp.company_info("Google", "Atlanta")
emp.employee_info(1200, "Software Developer")

"""
3. Multilevel inheritance
In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.
Example: 
Let’s create 3 classes namely, Vehicle, Car, SportsCar. Here, Vehicle is the superclass, Car is a child class of Vehicle, SportsCar is a child of Car. 
This is a good example of chaining in class/ Multilevel inheritance
"""
# Parent class to Car and GrandParent class to SportsCar
class Vehicle:
  def vehicle_info(self):
    print("Inside Vehicle class")

# child class and Parent Class to SportsCar
class Car(Vehicle):
  def car_info(self):
    print("Inside Car class")

# child class
class SportsCar(Car):
  def sports_car_info(self):
    print("Inside SportsCar class")

# create an object of SportsCar
ferrari = SportsCar()
# access Vehicle's and Car info using sportsCar object
ferrari.vehicle_info()
ferrari.car_info()
ferrari.sports_car_info()

"""
4. Hierarchical Inheritance
Hierarchical Inheritance is the right opposite of multiple inheritance. It means that there are multiple derived child classes from a single parent class.
Example:
Let’s create 'Vehicle' as a parent class and two child classes 'Car' and 'Truck' as a parent class
"""
# Parent class
class Vehicle:
  def vehicle_info(self):
    print("This is a Vehicle")

# child class
class Car(Vehicle):
  def car_info(self, name):
    print(f"Car name is: {name}")

# child class
class Truck(Vehicle):
  def truck_info(self, name):
    print(f"Truck name is: {name}")

# creating objects
obj1 = Car()
# access info
obj1.vehicle_info()
obj1.car_info("BMW")

obj2 = Truck()
# access info
obj2.vehicle_info()
obj2.truck_info("Ford")

"""
5. Hybrid Inheritance
Hybrid Inheritance is the mixture of two or more different types of inheritance. Here we can have many relationships between parent and child classes with multiple levels.
Example:
Let’s implement hierarchical and multiple inheritance combinations. 
Create a Parent class Vehicle and two child classes Car and Truck (hierarchical inheritance)
Create another class SportCar that inherits from two Parent classes named Car and Vehicle (Multiple inheritance)
# hybrid inheritance example
"""
# Parent class
class Vehicle:
  def vehicle_info(self):
    print("This is a Vehicle")

# child class
class Car(Vehicle):
  def car_info(self, name):
    print(f"Car name is: {name}")

# child class
class Truck(Vehicle):
  def truck_info(self, name):
    print(f"Truck name is: {name}")

# child class
class SportsCar(Car, Vehicle): # it has to be car first before vehicle
  def sports_car_info(self, name):
    print(f"Sports car name: {name}")

# create an object of SportsCar
ferrari = SportsCar()
# access Vehicle's and Car info using sportsCar object
ferrari.vehicle_info()
ferrari.car_info("ferrari")
ferrari.sports_car_info("porshe")

"""
Python super() function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent

Example:
In the example below, Let’s create a parent class Company and child class Employee. In Employee class, we call the parent class method by using a super() function.
"""
# Parent class
class Company:
  def company_name(self):
    return "Google"

# child class
class Employee(Company):
  def info(self, name):
    # calling the superclass method using super() function
    c_name = super().company_name()
    print(f"{name} works at {c_name}")

# create object of Employee
emp = Employee()
# access info
emp.info("Jessica")

"""
issubclass() 
In Python, we can verify whether a particular class is a subclass of another class. For this purpose, we can use Python built-in function issubclass(). This function returns True if the given class is the subclass of the specified class. Otherwise, it returns False.

Syntax:
issubclass(class, classinfo)
Where,
class: class to be checked.
classinfo: a class, type, or a tuple of classes or data types.
Example:
"""

class Company:
  def company_info(self):
    print("This is company class")

class Employee(Company):
  def emp_info(self):
    print("This is employee class")

class Player:
  def info(self):
    print("This is player class")

print(f"Is employee a subclass of company?: {issubclass(Employee, Company)}")
print(f"Is player a subclass of company?: {issubclass(Player, Company)}")
print(f"Is company a subclass of employee?: {issubclass(Company, Employee)}")

"""
More Resources
Python-Polymorphism: https://pynative.com/python-polymorphism/
Python-Encapsulation: https://pynative.com/python-encapsulation/
"""