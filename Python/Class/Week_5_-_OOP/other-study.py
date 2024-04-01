""" # What is setattr() used for?
The setattr() function in Python is used to set the value of a specified attribute of a given object. Let’s break down its purpose:
Setting an Attribute:
When you want to assign a value to an attribute (such as a variable) of an object dynamically, you can use setattr().
It allows you to modify an object’s attributes during runtime.
Syntax:
setattr(object, attribute, value)

object: The target object whose attribute you want to set.
attribute: The name of the attribute you want to modify.
value: The value you want to assign to the specified attribute.
Example Usage: Suppose we have a Person class with attributes name, age, and country:
"""
class Person:
  name = "John"
  age = 36
  country = "Norway"

# We can use setattr() to change the age attribute:
setattr(Person, 'age', 40)
"""
Other Related Functions:
getattr(): Retrieves the value of an attribute.
hasattr(): Checks if an attribute exists.
delattr(): Removes an attribute.
"""