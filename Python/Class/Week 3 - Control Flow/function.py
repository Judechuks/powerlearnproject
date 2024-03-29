# 1. Syntax of a function without parameters
# def <function_name()>:
  # <task to complete>

# 2. Syntax of a function with parameters
# def <function_name(a, b)>: # a, b - are the parameters
  # <task to complete>

# 1. without parameters
def add_nums():
  print("function without parameters", 2 + 13)
add_nums()

# 2. with parameters
def add_nums(a, b):
  print("function with parameters", a + b)
add_nums(20, 30)

# 3. without parameters and return value
def add_nums():
  return 20 + 5

addition = add_nums()
print("function without parameters & with return value", addition)

# 4. with parameters and return value
def add_nums(a, b):
  return a + b

addition = add_nums(20, 40)
print("function without parameters & with return value", addition)


"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
Lets see our above example, when number of arguments is unknown
"""
# if the number of arguments is unknown, add a "*" before the parameter name:
def add_nums(*nums):
  sum = 0
  for num in nums:
    sum += num
  return sum
print("Total:", add_nums(2, 5, 6, 7, 8, 13))


"""
Arbitrary Keyword Arguments, **kwargs
If the keyword arguments to be passed in a function are not known, you should add ** before the parameter name in the function definition. Example: **age
Example below demonstrates a function add_age() taking kwargs **age to calculate the sum of different people's ages.
"""
# if the number of kwargs is unknown, add a "**" before the parameter name:
def add_pages(**ages):
  sum = 0
  for k, v in ages.items(): # k = keyword, v = value
    sum += v
  return sum
print("Total: ", add_pages(mutemi=23, skinny=22, ahmed=21))