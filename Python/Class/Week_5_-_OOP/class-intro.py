"""
Python Classes/Objects
Python is a completely object-oriented language. You have been working with classes and objects right from the beginning of this course. 

Every element in a Python program is an object of a class, with its properties and methods. A Class is like an object constructor or a "blueprint" for creating objects.

A number, string, list, dictionary, etc., used in a program is an object of a corresponding built-in class. You can retrieve the class name of variables or objects using the type() method, 

>>> num=20
>>> type(num)
<class 'int'>            
>>> s="Python"
>>> type(s) 
<class 'str'>

Create a Class
A class in Python can be defined using the class keyword.

Syntax:

class <ClassName>:
    <statement1>
    <statement2>
    .
    .
    <statementN>

As per the syntax above, a class is defined using the class keyword followed by the class name and: operator after the class name, which allows you to continue in the next indented line to define class members.

The following are class members:

1. Class attributes
2. Constructor
3. Instance attributes
4. Properties
5. Class methods

A class can also be defined without any members. The following example defines an empty class using the pass keyword.

class Person:
  pass


Class Attributes
Class attributes are the variables defined directly in the class that are shared by all objects of the class. Class attributes can be accessed using the class name as well as using the objects.

class Person:
  name = 'Skinny' #Class attribute

Above, the name is a class attribute defined inside a class Person. The value of the name will remain the same for all the objects unless modified explicitly.

Accessing class attributes
>>> Person.name
'Skinny' 
>>> details = Person()
>>> details.name
'Skinny'

Constructor
In Python, the constructor method is invoked automatically whenever a new object of a class is instantiated, same as constructors in C++ or Java.
The constructor must have a special name __init__() and a special parameter called self. 
All classes have a function called __init__(), which is always executed when the class is being initiated.
The constructor in Python is used to define the attributes of an instance and assign values to them.
NB: The first parameter of each method in a class must be the self, which refers to the calling object. However, you can give any name to the first parameter, not necessarily self.

Example of how to define a constructor:

class Person:
  def __init__(self): # constructor method
    print('Constructor invoked')

Now, whenever you create an object of the Person class, the __init__() constructor method will be called, as shown below.

>>>details1 = Person()
Constructor invoked
>>>details2 = Person()
Constructor invoked

Instance Attributes
Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
The following example defines instance attributes name and age in the constructor.

class Person:
  nationality = 'Ethiopian' # class attribute
  def __init__(self): # constructor
    self.name = '' # instance attribute
    self.age = 0 # instance attribute

To access an instance variable, we use dot notation: 
[instance name].[attribute name], as shown below

>>> p1 = Person()
>>> p1.name
''
>>> p1.age
0

You can set the value of attributes using the dot notation, as shown below.
>>> p1 = Person()
>>> p1.name = "Mutemi" # assign value to instance attribute
>>> p1.age = 65    # assign value to instance attribute
>>> p1.name     # access instance attribute value
Mutemi
>>> p1.age     # access value to instance attribute
65

The best practice is to always specify the values of instance attributes through the constructor. 

Setting Attribute Values
The following constructor includes the name and age parameters, other than the self parameter.

class Person:
# name & age parameters passed in constructor
  def __init__(self, name, age): 
    self.name = name
    self.age = age

Passing Instance Attribute Values in Constructor
Now, you can specify the values while creating an instance, as shown below.

>>> p1 = Person('Mutemi', 65)
>>> p1.name
'Mutemi'
>>> p1.age
65

Setting Default Values of Instance Attributes
Also, you can set default values to instance attributes. By doing this, if the values are not provided when creating an object, the default values will be assigned.

Lets assign name="mkuu" and age=101
class Person:
  def __init__(self, name="Guest", age=101)
    self.name=name
    self.age=age

Instance Attribute Default Value
Now, you can create an object with default values, as shown below
>>> p1 = Person()
>>> p1.name
'Guest'
>>> p1.age
101

Class Methods
A python function in a class is called class method. Methods are defined using the def keyword. 
Each method must have a self as the first parameter, which refers to calling the instance.
Self is just a conventional name for the first argument of a method in the class.
A method defined as mymethod(self, a, b) should be called as x.mymethod(a, b) for the object x of the class.
Example: here we have a method named displayInfo

class Person:
  def displayInfo(self): # class method
    print('Personal Information')

The above class method can be called as a normal function, as shown below.

>>> p1 = Person()
>>> p1.displayInfo()
'Personal Information'

Let's combine our knowledge so far for class constructors and methods to access instance attributes using self parameter.

class Person:
  def __init__(self, name, age): # class constructor
    self.name = name 
    self.age = age 

  def displayInfo(self): # class method
    print('Person Name: ', self.name,', Age: ', self.age)


Calling a Method
Let's call/Invoke the displayInfo method as shown below:
>>> p1 = Person('Mutemi', 65)
>>> p1.displayInfo()
Person Name: Mutemi, Age: 65

"""