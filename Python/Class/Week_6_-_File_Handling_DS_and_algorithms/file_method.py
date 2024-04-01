"""
The open function returns a file object, which has several methods that can be used to manipulate the file. Some of the most commonly used methods are:

1. read: This method is used to read the contents of a file. By default, the read method reads the entire contents of the file and returns it as a string. If a number is passed as an argument to the read method, it reads that many characters from the file and returns them as a string.
2. write: This method is used to write to a file. The argument passed to the write method is written to the file as a string. If the file was opened in write mode ("w"), the contents of the file will be truncated and the new data will be written to the file. If the file was opened in append mode ("a"), the new data will be appended to the end of the file.
3. seek: This method is used to change the file pointer's position. The argument passed to the seek method is the number of bytes to move the file pointer. The seek method takes two optional arguments: the first argument is the number of bytes to move the file pointer, and the second argument is the starting point from where the file pointer should be moved. The starting point can be one of the following: 0 (the beginning of the file), 1 (the current position of the file pointer), or 2 (the end of the file).
4. tell: This method is used to return the current position of

Working with Files: Basic Syntax
One of the most important functions that you will need to use as you work with files in Python is open(), a built-in function that opens a file and allows your program to use it and work with it.
open(<file>, <mode>)

First Parameter: File
The first parameter of the open() function is file, the absolute or relative path to the file that you are trying to work with.
We usually use a relative path, which indicates where the file is located relative to the location of the script (Python file) that is calling the open() function.

Second Parameter: Mode

The second parameter of the open() function is the mode, a string with one character. That single character basically tells Python what you are planning to do with the file in your program.

Modes available are:

Read ("r").
Append ("a")
Write ("w")
Create ("x")

You can also choose to open the file in:
Text mode ("t")
Binary mode ("b")
To use text or binary mode, you would need to add these characters to the main mode. For example: "wb" means writing in binary mode.
💡 Tip: The default modes are read ("r") and text ("t"), which means "open for reading text" ("rt"), so you don't need to specify them in open() if you want to use them because they are assigned by default. You can simply write open(<file>).

Why Modes?
It really makes sense for Python to grant only certain permissions based what you are planning to do with the file, right? Why should Python allow your program to do more than necessary? This is basically why modes exist.
Think about it — allowing a program to do more than necessary can problematic. For example, if you only need to read the content of a file, it can be dangerous to allow your program to modify it unexpectedly, which could potentially introduce bugs.

🔸 How to Read a File
Now that you know more about the arguments that the open() function takes, let's see how you can open a file and store it in a variable to use it in your program.

This is the basic syntax:
<var> = open(<filename>, mode>)
We are simply assigning the value returned to a variable. For example:
file_object = open("example.txt", "r") # method read
file_object.close() # closing

I know you might be asking: what type of value is returned by open()?
Well, a file object.
Let's talk a little bit about them.


File Objects
According to the Python Documentation, a file object is:
An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource.
This is basically telling us that a file object is an object that lets us work and interact with existing files in our Python program.

File objects have attributes, such as:
🔸name: the name of the file.
🔸closed: True if the file is closed. False otherwise.
🔸mode: the mode used to open the file.

Syntax:
<file_object>.<attribute>
For example:
print(fileObj.name) # name
print(fileObj.closed) # closed
print(fileObj.mode) # mode

Methods to Read a File
For us to be able to work with file objects, we need to have a way to "interact" with them in our program and that is exactly what methods do. Let's see some of them.

Read()
The first method that you need to learn about is read(), which returns the entire content of the file as a string.
<file_obj>.read([size]) # size is optional dictates how many bytes to read
Here we have an example:
file_object = open(filename, mode)
file_content = file_object.read()
file_object.close()
print(file_content)

1. filename is the name of the file you want to read.
2. mode is the mode in which you want to open the file (e.g., 'r' for read mode).
3. file_object is the file object that represents the file.
4. file_contents is the string that contains the entire contents of the file.

You can use the type() function to confirm that the value returned by f.read() is a string:

f = open("example.txt", "r")
file_contents = f.read()
f.close()
print(type(file_content))

❗️Important: You need to close a file after the task has been completed to free the resources associated to the file. To do this, you need to call the close() method, like this:
<file_obj>.close()


Readline() vs. Readlines()
You can read a file line by line with these two methods. They are slightly different, so let's see them in detail.
readline() reads one line of the file until it reaches the end of that line. A trailing newline character (\n) is kept in the string.

💡 Tip: Optionally, you can pass the size, the maximum number of characters that you want to include in the resulting string.
<file_obj>.readline([size]) # size is optional dictates how many bytes to read
For example:
This is the first line of the file.

In contrast, readlines() returns a list with all the lines of the file as individual elements (strings). This is the syntax:
<file_obj>.readlines([size]) # size is optional dictates how many bytes to read

Those are the main methods used to read file objects. Now let's see how you can create files.

🔹 How to Create a File
If you need to create a file "dynamically" using Python, you can do it with the "x" mode.
Let's see how. This is the basic syntax:
<var> = open("<filename>.<extention>", "x") # x denotes create the file
Example:
file_obj = open("filename.txt", "x")
file_obj.close()

With this mode, you can create a file and then write to it dynamically using methods that you will learn in just a few moments.

💡 Tip: The file will be initially empty until you modify it.
A curious thing is that if you try to run this line again and a file with that name already exists, you will see this error:

🔸 How to Modify a File
To modify (write to) a file, you need to use the write() method. You have two ways to do it (append or write) based on the mode that you choose to open it with. Let's see them in detail.

1. Append
"Appending" means adding something to the end of another thing. The "a" mode allows you to open a file to append some content to it.

For example, if we have this file: (names.text - containing names of people, one per a line)
And we want to add a new line to it, we can open it using the "a" mode (append) and then, call the write() method, passing the content that we want to append as argument.
This is the basic syntax to call the write() method:
<file_obj>.write(<string>) # string = content that you want to append
Here's an example:
file_obj = open("filename.txt", "a")
file_obj.write("\n New Line")
file_obj.close()

💡 Tip: Notice that I'm adding \n before the line to indicate that I want the new line to appear as a separate line, not as a continuation of the existing line.

💡 Tip: The new line might not be displayed in the file until f.close() runs.

2. Write
Sometimes, you may want to delete the content of a file and replace it entirely with new content. You can do this with the write() method if you open the file with the "w" mode.

Here we have this text file: (names.text - containing names of people, one per a line)
If I run this script:
f = open("data/names.txt", "w")
f.write("New Content")
f.close()

result: It removes the content of the file and replaces it with "New Content" in first line

As you can see, opening a file with the "w" mode and then writing to it replaces the existing content.

💡 Tip: The write() method returns the number of characters written.

If you want to write several lines at once, you can use the writelines() method, which takes a list of strings. Each string represents a line to be added to the file.

Here's an example. This is the initial file: (names.text - containing names of people, one per a line)
If we run this script:
f = open("data/names.txt", "a")
f.writelines(["\nline1", "\nline2", "\nline3"])
f.close()

Open File For Multiple Operations
Now you know how to create, read, and write to a file, but what if you want to do more than one thing in the same program? Let's see what happens if we try to do this with the modes that you have learned so far:
If you open a file in "r" mode (read), and then try to write to it:

with open("example.txt", "r") as file:
  file.write("Hello, world!")
Output: UnspupportedOperation: not writable

The same will occur with the "a" (append) mode.
How can we solve this? To be able to read a file and perform another operation in the same program, you need to add the "+" symbol to the mode, like this:

with open("example.txt", "r+") as file:
  contents = file.read()
  file.write("Hello, world!")

In this example, we first read the contents of the file using the read() method, and then write to the file using the write() method.
Note that when you open a file in "r+" mode, the file pointer is initially positioned at the beginning of the file. If you want to append to the end of the file, you should open the file in "a+" mode instead.
Very useful, right? This is probably what you will use in your programs, but be sure to include only the modes that you need to avoid potential bugs.

Sometimes files are no longer needed. Let's see how you can delete files using Python.

🔹 How to Delete Files
To remove a file using Python, you need to import a module called "os" which contains functions that interact with your operating system.

💡 Tip: A module is a Python file with related variables, functions, and classes.

Particularly, you need the remove() function. This function takes the path to the file as argument and deletes the file automatically.

import os  # import statement
os.remove(<file>)  # function call

Let's see an example. We want to remove the file called sample_file.txt.
To do it, we write this code:

import os 
filename = "example.txt"
if os.path.exists(filename): # check if the file exists
  os.remove(filename) # delete the file
  print(f"{filename} has been deleted.")
else:
  print(f"{filename} does not exist.")

The first line: import os is called an "import statement". This statement is written at the top of your file and it gives you access to the functions defined in the os module.
The second line: os.remove("sample_file.txt") removes the file specified.
💡 Tip: you can use an absolute or a relative path.

Now that you know how to delete files, let's see an interesting tool... Context Managers!

🔸 Meet Context Managers
Context Managers are Python constructs that will make your life much easier. By using them, you don't need to remember to close a file at the end of your program and you have access to the file in the particular part of the program that you choose.

Syntax:
This is an example of a context manager used to work with files:
with open("<file>", "<mode">) as <var>:
  # do what you need with the file

💡 Tip: The body of the context manager has to be indented, just like we indent loops, functions, and classes. If the code is not indented, it will not be considered part of the context manager.
When the body of the context manager has been completed, the file closes automatically.
Example:
class MyContextManager:
  def __enter__(self):
    print("Entering context")
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    print("Exiting context")
    if exc_type is not None:
      print(f"An error of type {exc_type} occurred: {exc_val}")
    return True

with MyContextManager() as cm:
  print("Inside context")
  # code that may raise an exception

In this example, the MyContextManager class defines the __enter__() and __exit__() methods to be used as context managers. The __enter__() method is called when the block is entered, and the __exit__() method is called when the block is exited, either normally or due to an exception.
When an exception occurs inside the block, the __exit__() method is called with the exception type, value, and traceback as arguments. If the __exit__() method returns True, the exception is considered handled and the program continues. If it returns False or raises another exception, the original exception is propagated.

with open("data/names.txt", "r+") as f:
  print(f.readlines())

This context manager opens the names.txt file for read/write operations and assigns that file object to the variable f. This variable is used in the body of the context manager to refer to the file object.

Trying to Read it Again
After the body has been completed, the file is automatically closed, so it can't be read without opening it again. But wait! We have a line that tries to read it again, right here below:

with open("data/names.txt", "r+") as f:
  print(f.readlines())
print(f.readlines()) # Trying to read the file again, outsideof the context manager

Let's see what happens:

Traceback (most recent call last):
  File "<path>", line 21, in <module>
    print(f.readlines())
ValueError: I/O operation on closed file.

ValueError: I/O operation on closed file.
This error is thrown because we are trying to read a closed file. Awesome, right? The context manager does all the heavy work for us, it is readable, and concise.
"""