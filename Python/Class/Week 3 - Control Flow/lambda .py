"""
What is the Lambda function in python?
A lambda function is a special type of function without a name. That is why it's referred to as an anonymous function.
Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement. They're also useful when you want to use the function once.
Python lambda Function Declaration
We use the lambda keyword instead of def to create a lambda function.
Syntax:
lamba argument(s): expression
or
lamba <function_parameter>: <return_value>
"""

snack = lambda : print("Pizza!")
snack()

# Note: Lambda function can take any number of arguments but can only have one expression.
num_square = lambda num : num ** 2
print(f"Square of num is: {num_square(8)}")