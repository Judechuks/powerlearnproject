"""
Understaning the use of python library PANDAS
Data manipulation and analysis library for working with structured data.
❗️ Pandas is a popular open-source library for data manipulation and analysis in Python. It provides data structures and functions for working with structured data, such as tables of numerical and textual data. Pandas is built on top of the NumPy library, which provides efficient array operations in Python.
Pandas provides two main data structures: 
💡 Series and DataFrame. 
A Series is a one-dimensional array-like object that can hold any data type. It has an associated index, which labels each element in the Series. 
A DataFrame is a two-dimensional table-like structure that contains rows and columns of data. It is similar to a spreadsheet or a SQL table. Each column in a DataFrame is a Series.

Pandas provides a wide range of functions for reading and writing data to and from various file formats, including CSV, Excel, SQL databases, and more. It also provides functions for data cleaning, filtering, sorting, merging, and grouping.

Here are some examples of what you can do with Pandas:
1. Load data from a CSV file into a DataFrame
2. Filter and sort data in a DataFrame based on certain criteria
3. Compute summary statistics of the data, such as mean, median, and standard deviation
4. Aggregate data using group-by operations
5. Visualize data using built-in plotting functions

❗️ Pandas is widely used in data science, finance, and other fields where data analysis is an important part of the work. Its intuitive syntax and powerful functionality make it a popular choice for working with structured data in Python.
"""
# 1. Creating a Pandas DataFrame:
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
       }
df = pd.DataFrame(data)
print(df)

# 2. Reading data from a CSV file into a Pandas DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# 3. Selecting data from a Pandas DataFrame:
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
       }
df = pd.DataFrame(data)
# select a single column
print(df['name'])
# select a multiple column
print(df[['name', 'age']])
# select row by index
print(df.loc[0])
# select rows by condition
print(df[df['age'] > 30])

# 4. Adding a new column to a Pandas DataFrame:
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
       }
df = pd.DataFrame(data)
# Add a new column
df['salary'] = [50000, 60000, 70000 ]
print(df)

# 5. Grouping data in a Pandas DataFrame:
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
       }
df = pd.DataFrame(data)
# Add a new column
df['salary'] = [50000, 60000, 70000 ]
# Group by age and get the average salary for each group
grouped = df.groupby('age')['salary'].mean()
print(grouped)

"""
OUTPUT:
age
25      50000.0
30      60000.0
35      70000.0
Name: salary, dtype: float64


These are just a few examples of the many things you can do with Pandas in Python. Pandas is a powerful library for data manipulation and analysis, and it is widely used in data science, finance, and other fields.
"""