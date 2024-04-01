"""
Input and Output in Python refer to the process of taking input from the user and displaying output to the user. The input function is used to take input from the user, and the print function is used to display output to the user.
Here's a simple example to illustrate this: 
"""
name = input("Enter your name: ")
print(f"Hello, {name}")
"""
In this example, the input function takes a string argument (prompt) which is displayed to the user, and it returns the user's input as a string. The input function is used to take input from the user and store it in a variable. The print function is used to display output to the user by printing its argument(s).
Another explanation is that
Input and Output in Python are two important concepts that are used to interact with the user.
Input refers to the process of taking data from the user and storing it in a program for further processing. This can be done using the input function in Python. The input function takes a string argument (prompt) which is displayed to the user, and it returns the user's input as a string.

name = input("What is your name?: ")
age = input("What is your age?: ")

In the above code, the input function is used to prompt the user to enter their name and age. The input data is then stored in the variables' names and ages, respectively.
The print function, on the other hand, is used to display output to the user by printing its argument(s) to the screen. The argument(s) can be a string, variable, or expression. For example:

print("Hello, ", + name + "! You are " + age + " years old.")

Output refers to the process of displaying the result of a computation or a processing step to the user. This can be done using the print function in Python. The print function is used to display output to the user by printing its argument(s).

In addition to the input and print functions, there are other ways to handle Input-Output in Python, such as reading and writing to files, using command line arguments, or using third-party libraries.
Why do we use Input and Output in Python:
Input and Output are used in Python to allow the user to interact with the program. The use of Input and Output enables the program to receive data from the user and provide results to the user.
Here are some common use cases for Input and Output in Python:

1. Taking input from the user: The input function is used to take input from the user, such as a name, age, or any other type of data. The input received from the user can be stored in a variable for further processing.

2. Displaying output to the user: The print function is used to display output to the user. This can be used to display the result of a calculation, the contents of a list or dictionary, or any other type of data.

3. Reading data from a file: Input can also be taken from a file, such as a text file, CSV file, or any other type of file. This can be done using the open function in Python or using third-party libraries like Pandas.

4. Writing data to a file: Output can also be stored in a file, such as a text file, CSV file, or any other type of file. This can be done using the open function in Python or using third-party libraries like Pandas.

Input and Output are essential in making the program more interactive and user-friendly. They also allow the program to receive and provide data, which is crucial for many applications.


Python (Files I/O)
1. Understanding how to read and write files:
In Python, reading from and writing to files can be accomplished using the open function. The open function takes two arguments: the name of the file and the mode in which the file should be opened.

There are four modes in which a file can be opened in Python:
1. "r" (Read Only): This mode is used to only read the contents of a file. If the file does not exist, a FileNotFoundError will be raised.
2. "w" (Write Only): This mode is used to write to a file. If the file already exists, its contents will be truncated (i.e., deleted), and a new file with the same name will be created. If the file does not exist, a new file with the specified name will be created.
3. "a" (Append Only): This mode is used to append to an existing file. If the file does not exist, a new file with the specified name will be created.
4. "x" Create (Write Only, Exclusive Creation): This mode is used to write to a file only if the file does not already exist. If the file already exists, a FileExistsError will be raised.

Here's an example of how to read from a file in Python:
"""
# open file for reading
file = open("example.txt", "r")
# read the content of the file
content = file.read()
# print the content of the file
print(content)
# close the file
file.close ()

"""And here's an example of how to write to a file in Python:"""
# open file for writing
file = open("example-copy.txt", "w")
# write some text to the file
file.write("Hello, this is written from read_and_write.py code\n")
file.write("Just for testing.\n")
# close the file
file.close ()

# It's recommended to use the with the statement when opening files in Python, as it automatically takes care of closing the file when the code block is exited, even if an exception is raised

"""
Reading Keyboard Input
Python provides two built-in functions to read a line of text from standard input, which by default comes from the keyboard. These functions are:
1. raw_input
2. input

The raw_input Function
The raw_input([prompt]) function reads one line from standard input and returns it as a string (removing the trailing newline).

Flat Files vs. Non-Flat Files
Flat files are data files that contain records with no structured relationships between the records, and there's also no structure for indexing like you typically find it in relational databases. These files can contain only basic formatting, have a small fixed number of fields, and can or can not have a file format.


Python File Objects
Python has in-built functions to create, read, write, and manipulate accessible files. The io module is the default module for accessing files that can be used off the shelf without even importing it. Before you read, write, or manipulate the file, you need to make use of the module open(filename, access_mode) that returns a file object called "handle". After which you can simply use this handle to read from or write to a file. Like everything else, files in Python are also treated as an object, which has its own attributes and methods.
An IOError exception is raised if, while opening the file, the operation fails. It could be due to various reasons like trying to read a file that is opened in write mode or accessing a file that is already closed.
As you already read before, there are two types of flat files, text and binary files:
As you might have expected from reading the previous section, text files have an End-Of-Line (EOL) character to indicate each line's termination. In Python, the new line character (\n) is the default EOL terminator.
Since binary files store data after converting it into a binary language (0s and 1s), there is no EOL character. This file type returns bytes. This file is used when dealing with non-text files such as images, .exe, or .pyc.
Let's now understand the Python file objects in detail, along with necessary examples.

Open()
The built-in Python function open() has the following arguments: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) The open() function has almost 8 parameters along with their default values for each argument as shown above.
You would be focusing on the first and second parameters for now, which are essential for reading and writing files. And go through other parameters one by one as the tutorial progresses.
Let's understand the first argument, i.e., file.

File
file is a mandatory argument that you have to provide to the open function while the rest of the arguments are optional and use their default values.
To put it simply, the file argument represents the path where your file resides in your system.
If the path is in the current working directory, you can just provide the filename. If not then you have to provide the absolute path of the file, just like in the following examples: my_file_handle=open("mynewtextfile.txt") If the file resides in a directory other than the current directory, you have to provide the absolute path with the file name:
myfilehandle = open(/path/to/mynewtextfile.txt)

Let's understand the second argument of the open function, i.e., access modes.

Access Modes
Access modes define in which way you want to open a file, whether you want to open a file in:
+ read-only mode
+ write-only mode
+ append mode
+ both read and write mode
Though a lot of access modes exist as shown in the below table, the most commonly used ones are read and write modes. It specifies where you want to start reading or writing in the file.
You use 'r', the default mode, to read the file. In other cases where you want to write or append, you use 'w' or 'a', respectively.
There are, of course, more access modes! Take a look at the following table:
character| function
-------------------------------------------------------------------------------------------------
r        | open file for reading only. Starts reading from beginning of the file. its default mode.
rb       | open file for reading only in binary format. Starts reading from beginning of the file.
r+       | open file for reading and writing. File pointer placed at beginning of the file.
w        | open file for writing only. File pointer placed at beginning of the file. Overwrites existing file and creates a new one if it does not exists.
wb       | same as w but opens in binary mode.
w+       | same as w but also allows to read from file.
wb+      | same as wb but also allows to read from file.
a        | open a file for appending. Starts writing at end of file. Creates a new file if the file does not exist.
ab       | same as 'a' but in a binary format. Creates a new file if file does not exist
a+       | same as 'a' but also open for reading.
ab+      | same as 'ab' but also open for reading in binary mode.

As you have seen in the first section, there are two types of flat files. This is also why there's an option to specify which format you want to open, such as text or binary. Of course, the former is the default. When you add 'b' to the access modes, you can read the file in binary format rather than the default text format. It is used when the file to be accessed is not in text format.
"""