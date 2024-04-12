"""
Modules
Any Python source file is a module.

# foo.py code:
def grok(a):
  ...
def spam(b):
  ...

An import statement loads and executes a module.

# program.py code:
import foo
a = foo.grok(2)
b = foo.spam("Hello")

Packages vs Modules
For larger collections of code, it is common to organize modules into a package.
# From this
pcost.py
report.py
fileparse.py

# To this
porty/
    __init__.py
    pcost.py
    report.py
    Fileparse.py

You pick a name and make a top-level directory. porty in the example above (clearly picking this name is the most important first step).
Add an __init__.py file to the directory. It may be empty.
Put your source files into the directory.

Using a Package
A package serves as a namespace for imports.
This means that there are now multilevel imports.
# 1. code 
import porty.report
port = porty.report.read_portfolio('portfolio_csv')

There are other variations of import statements
# 2. code
from porty import report
port = report.read_portfolio('portfolio_csv')

# 3. code
from porty.report import read_portfolio
port = read_portfolio('portfolio_csv')

Two Problems
There are two main problems with this approach.
1. imports between files in the same package break.
2. Main scripts placed inside the package break.
So, basically everything breaks. But, other than that, it works

Problem 1: Imports
Imports between files in the same package must now include the package name in the import. Remember the structure.

porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py

Modified import example.
# report.py
from porty import fileparse
def read_portfolio(filename):
  return fileparse.parse_csv(...)

All imports are absolute, not relative.
# report.py
import fileparse  # BREAKS. fileparse not found

Relative: Imports
Instead of directly using the package name, you can use . to refer to the current package.
syntax:
from . import module_name
# code
from . import fileparse
def read_portfolio(filename):
  return fileparse.parse_csv(...)

Problem 2: Main scripts
Running a package submodule as a main script breaks.
bash $ python porty/pcost.py # BREAKS

Reason: You are running Python on a single file and Python doesn't see the rest of the package structure correctly (sys.path is wrong).

All imports break. To fix this, you need to run your program in a different way, using the -m option.

bash $ python -m porty.pcost # WORKS

__init__.py files
The primary purpose of these files is to stitch modules together.

Example: consolidating functions
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
# this make names appear at the top-level while importing
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
# instead of using the multilevel imports
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
"""