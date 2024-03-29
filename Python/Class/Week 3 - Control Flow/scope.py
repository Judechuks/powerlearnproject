"""
1. Local Scope
Local scope refers to a variable declared inside a function. For example, in the code below, the variable total is only available to the code within the add_nums function. Anything outside of this function will not have access to it.

2. Enclosing scope
Enclosing scope refers to a function inside another function or what is commonly called a nested function. 
In the code below, I added a nested function called double_it to the add_nums function.
As double_it is inside the scope for the add_nums function it can then access the variable. However, the enclosed variable inside the double_it function cannot be accessed from inside the add_nums function.

3. Global scope
Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere.
In the code below, I added a global variable called global_var. This can then be accessed from both functions add_nums and double_it:

4. Built-in scope
Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth. Functions with built-in scope can be accessed at any level.
"""

# Example:
global_var = 13

def add_nums(a, b):
  # enclosed scope variable declared inside a function
  total = a + b
  print(f"Global_var in outer function: {global_var}")
  def double_it():
    # local variable
    double = total * 2
    print(f"Global_var in inner function: {global_var}")
    print(f"Double: {double}")
  double_it()
  return total

add_nums(14, 6)