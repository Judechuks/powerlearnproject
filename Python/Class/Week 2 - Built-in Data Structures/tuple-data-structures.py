"""
Tuples
A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.
We can use the type() function to know which class a variable or a value belongs to.
"""
var1 = ("Hello")
print(type(var1)) # <class 'str'>
var2 = ("Hello",)
print(type(var2)) # <class 'tuple'>
var3 = "Hello",
print(type(var3)) # <class 'tuple'>
"""
Here,
("hello") is a string so type() returns str as class of var1 i.e. <class 'str'>
("hello",) and "hello", both are tuples so type() returns tuple as class of var1 i.e. <class 'tuple'>

Accessing Elements
1. Indexing: using [index] of the element
2. Negative Indexing: using [-index], e.g -1 = last item, -2 = second to the last item and so on.
"""