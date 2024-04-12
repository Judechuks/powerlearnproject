"""
Python Packages
In Python, a package is a way of organizing related modules into a single directory hierarchy. A package is simply a directory that contains a special file called __init__.py, which can be empty or can contain Python code to initialize the package. (you can also check the package-module.py file)

To create a package, you can create a new directory and add an empty __init__.py file to it. Then you can create one or more Python modules in the same directory, and they will be treated as part of the package. 

For example, suppose you create a directory called mypackage, and add an empty __init__.py file to it. Then you create two Python modules called module1.py and module2.py in the same directory. You can then import the modules using the package name, like this:

Alternatively, you can use the from ... import ... statement to import specific names from the modules:
This allows you to organize related code into a single package, and makes it easier to import and manage the code in larger projects. Many popular Python libraries, such as NumPy and pandas, are organized as packages


Package Model Structure in Python Programming
In Python, a package is a way of organizing related modules into a single directory hierarchy. The structure of a package can be visualized as a tree, where the package is the root node, and the modules are the leaf nodes. Here's an example of a typical package structure:
In this example, the package directory is called mypackage, and it contains two modules (module1.py and module2.py) and a subpackage directory called subpackage. The subpackage directory also contains an __init__.py file to initialize the subpackage, and a single module called module3.py
To import a module from a package, you use the dot notation to specify the package and module names. For example:
Or you can use the from ... import ... statement to import specific names from the module:
This allows you to organize related code into a hierarchy of packages and subpackages, and makes it easier to import and manage the code in larger projects.


Package initialization
Package initialization refers to the process of setting up a software package or library before it can be used by an application or program. This typically involves loading any necessary dependencies, setting up configuration options, and executing any initialization code or routines. In many programming languages, package initialization is triggered automatically when the package is imported or referenced by a program.

If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.

For example, consider the following __init__.py file:
__init__.py
print(f"Invoking __init__.py for {__name__}")
A = ["Janet", "Joy", "Judith"]
Let’s add this file to the pkg directory from the above example:
pkg folder
  __init__.py
  mod1.py
  mod2.py

Now when the package is imported, the global list A is initialized:
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.A
["Janet", "Joy", "Judith"]

A module in the package can access the global variable by importing it in turn:
mod1.py
def foo():
  from pkg import A
  print('[mod1] foo() / A = ', A)

  class Foo:
    pass

running the code
>>> from pkg import mod1
Invoking __init__.py for pkg
>>> mod1.foo()
[mod1] foo() / A = ["Janet", "Joy", "Judith"]

__init__.py can also be used to effect automatic importing of modules from a package. For example, earlier you saw that the statement import pkg only places the name pkg in the caller’s local symbol table and doesn’t import any modules. But if __init__.py in the pkg directory contains the following:

__init__.py
print(f"Invoking __init__.py for {__name__}")
import pkg.mod1, pkg.mod2

then when you execute import pkg, modules mod1 and mod2 are imported automatically:
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.mod1.foo()
[mod1] foo()
>>> pkg.mod2.bar()
[mod2] bar()
"""