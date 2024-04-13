"""
NumPy: Numerical computing library for working with arrays and matrices
NumPy arrays are a fundamental data structure in the NumPy library, which is a powerful tool for numerical computing in Python. A NumPy array is similar to a Python list, but it has the following properties:

1. Homogeneous data type: All elements of a NumPy array must have the same data type, which is typically a numeric data type such as int or float.
2. Fixed size: The size of a NumPy array is fixed when it is created, and it cannot be changed without creating a new array.
3. Efficient: NumPy arrays are designed to be efficient for numerical operations, and they are implemented in C, which makes them faster than Python lists.
NumPy arrays can have one or more dimensions, and they are represented in memory as contiguous blocks of data. This makes it possible to perform mathematical operations on the entire array at once, rather than looping over individual elements

Creating a NumPy array:
"""
import numpy as np
a = np.array([1,2,3])
print(a)
"""
In this example, we create a NumPy array with three elements and print it to the console. NumPy arrays can be used for a wide variety of numerical computing tasks, including linear algebra, statistics, and signal processing, among others.
"""
# Creating a 2D NumPy array:
import numpy as np
b = np.array([[1,2,3], [2,4,6]])
print(b)

# Using NumPy functions to perform mathematical operations on arrays:
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
# Addition
print(a + b) # [5, 7, 9]
# Subtraction
print(a - b) # [-3, -3, -3]
# Multiplication
print(a * b) # [4, 10, 18]
# Division
print(b / a) # [4.0, 2.5, 2.0]


# Slicing and indexing NumPy arrays:
import numpy as np
d = np.array([1, 2, 3, 4, 5])
# Indexing
print(d[0]) # 1
print(d[-1]) # 5
# Slicing
print(d[1:4]) # 2,3,4

# Reshaping NumPy arrays:
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshaping into 3x3 array
b = a.reshape((3,3))
"""
output: [[1,2,3]
         [4,5,6]
         [7,8,9]]

These are just a few examples of the many things you can do with NumPy in Python. NumPy is a powerful library for scientific computing, and it is widely used in data analysis, machine learning, and other fields.
"""
