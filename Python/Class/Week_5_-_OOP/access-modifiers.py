"""
Access modifiers
Access modifiers play an important role in securing the data from unauthorized access and preventing any data exploitation.
Using the underscore (_), we can control access to the data inside the Python classes. Python Class has three types of access modifiers:
1. Public Access Modifier
2. Private Access Modifier
3. Protected Access Modifier

1. Public Members
The name "Public" says all about this access modifier: the variables and methods declared inside the specific Python class can be accessed by that class and any Python class outside that specific class.
Public methods are accessible outside the class and with the help of objects the public methods can be invoked inside the class.
All members in a Python class are public by default. Any member can be accessed from outside the class environment.
Example:
"""
# example of public attribute
class Student:
  schoolName = "PLP academy" # class attribute

  def __init__(self, name, age):
    self.name = name # instance attribute
    self.age = age # instance attribute

# How to access public members
student1 = Student("Jessica", 26)
print(f"{student1.name} attends {student1.schoolName} at the age of {student1.age}") # accessing members publicly
student1.age = 28 # modified the age to 28
print(f"By the time she graduates she will be {student1.age}")
# You can access the Student class's attributes and also modify their values, as shown above.

"""
2. Protected Members
Protected members of a class are accessible from within the class and are also available to its subclasses. No other environment is permitted access to it. 
This enables specific resources of the parent class to be inherited by the child class.
Conventionally, to make an instance variable protected you add a prefix _ (single underscore) to it. This effectively prevents it from being accessed unless it is from within a sub-class.
Example:
"""
# example of protected attribute (Note the use of underscore)
class Student:
  _schoolName = "Milestone academy" # protected class attribute

  def __init__(self, name, age):
    self._name = name # protected instance attribute
    self._age = age # protected instance attribute

# How to access protected members
student2 = Student("Jude", 26)
print(f"{student2._name} attends {student2._schoolName} at the age of {student2._age}") # accessing members publicly
student2._age = 28 # modified the age to 28
print(f"By the time he graduates he will be {student2._age}")

"""
3. Private Members
You can make an instance variable or method private by using the double underscore __, like:
"""
# example of private attribute (Note the use of double underscore)
class Student:
  __schoolName = "Mastermind academy" # private class attribute

  def __init__(self, name, age):
    self.__name = name # private instance attribute
    self.__age = age # private instance attribute

  def __display(self): # private method
    print("This is a private method")
"""
Python performs name mangling of private variables. Every member with a double underscore will be changed to _object._class__variable. So, it can still be accessed from outside the class, but the practice should be refrained.
"""
# How to access private members (notice how the class name was included to the members starting with underscore)
student3 = Student("James", 27)
student3._Student__display()
print(f"{student3._Student__name} attends {student3._Student__schoolName} at the age of {student3._Student__age}") # accessing members publicly
student3._Student__age = 29 # modified the age to 29
print(f"By the time he graduates he will be {student3._Student__age}")