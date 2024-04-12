"""
Getting Started With Python Modules
Python modules are reusable pieces of code that can be imported into a program to provide additional functionality. They are usually written in Python and can be either built-in modules or third-party modules that can be installed using tools like pip. Modules can contain functions, classes, variables, and constants that can be accessed by importing them into a Python script. Some popular built-in modules include math, datetime, and random, while popular third-party modules include pandas, NumPy, and matplotlib.

As our program grows bigger, it may contain many lines of code. Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionality. This makes our code organized and easier to maintain.

Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc. Let's see an example,

Let us create a module. Type the following and save it as example.py.
"""
def add(a, b):
  return a + b
print(f"4 + 6 = {add(4, 6)}")

"""
Here, we have defined a function add() inside a module named example. The function takes in two numbers and returns their sum.

Import modules in Python
We can import the definitions inside a module to another module or the interactive interpreter in Python.
We use the import keyword to do this. To import our previously defined module example, we type the following in the Python prompt.
import example

This does not import the names of the functions defined in example directly in the current symbol table. It only imports the module name example there.

Using the module name we can access the function using the dot . operator. For example:
example.add(4,6) # returns 9

Import Python Standard Library Modules
The Python standard library contains well over 200 modules. We can import a module according to our needs.
To import a module from the Python Standard Library, you can use the import statement followed by the name of the module. Here's an example of how to import the math module:
import math

You can then access the functions and constants defined in the math module using the . notation. For example, to use the sqrt function to find the square root of a number, you could write:
x = math.sqrt(25)
print(x)

This would output 5.0, which is the square root of 25. There are many modules in the Python Standard Library, and you can find a list of them in the Python documentation.


Python import with Renaming
In Python, we can also import a module by renaming it. For example,
"""
# importing module by renaming it
import math as m
print("Pie =", m.pi)

"""
Here, We have renamed the math module as m. This can save us typing time in some cases.
Note that the name math is not recognized in our scope. Hence, math.pi is invalid, and m.pi is the correct implementation.


Python from...import statement
We can import specific names from a module without importing the module as a whole. For example,
"""
# importing only  pi from math module
from math import pi
print("Pie =", pi)
"""
Here, we imported only the pi attribute from the math module.

Import all names
In Python, we can import all names(definitions) from a module using the following construct:
"""
# import all names from the standard module math
from math import *
print("The value of pie is", pi)
"""
Here, we have imported all the definitions from the math module. This includes all names visible in our scope except those beginning with an underscore(private definitions).
Importing everything with the asterisk (*) symbol is not a good programming practice. This can lead to duplicate definitions for an identifier. It also hampers the readability of our code.
"""