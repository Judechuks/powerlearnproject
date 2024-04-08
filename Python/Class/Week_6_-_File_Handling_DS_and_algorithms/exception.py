"""
Exceptions are raised when the program encounters an error during its execution. They disrupt the normal flow of the program and usually end it abruptly. To avoid this, you can catch them and handle them appropriately.

You've probably seen them during your programming projects.
If you've ever tried to divide by zero in Python, you must have seen this error message:
If you tried to index a string with an invalid index, you definitely got this error message:
These are examples of exceptions.

Common Exceptions
There are many different types of exceptions, and they are all raised in particular situations. Some of the exceptions that you will most likely see as you work on your projects are:

IndexError - raised when you try to index a list, tuple, or string beyond the permitted boundaries.
KeyError - raised when you try to access the value of a key that doesn't exist in a dictionary.
NameError - raised when a name that you are referencing in the code doesn't exist. For example:
TypeError - raised when an operation or function is applied to an object of an inappropriate type.
ZeroDivisionError - raised when you try to divide by zero.

💡 Tips: To learn more about other types of built-in exceptions, please refer to this article in the Python Documentation.

Anatomy of an Exception
I'm sure that you must have noticed a general pattern in these error messages. Let's break down their general structure piece by piece:
First, we find this line (see below). A traceback is basically a list detailing the function calls that were made before the exception was raised.
The traceback helps you during the debugging process because you can analyze the sequence of function calls that resulted in the exception:
Traceback (most recent call last):
Then, we see this line (see below) with the path to the file and the line that raised the exception. In this case, the path was the Python shell <pyshell#0> since the example was executed directly in IDLE.

File "<pyshell#0>", line 1, in <module>
a - 5/0

💡 Tip: If the line that raised the exception belongs to a function, <module> is replaced by the name of the function.

Finally, we see a descriptive message detailing the type of exception and providing additional information to help us debug the code:
NameError: name 'a' is not defined


Exception Handling: Purpose & Context
You may ask: why would I want to handle exceptions? Why is this helpful for me? By handling exceptions, you can provide an alternative flow of execution to avoid crashing your program unexpectedly.

Example: User Input
Imagine what would happen if a user who is working with your program enters an invalid input. This would raise an exception because an invalid operation was performed during the process.
If your program doesn't handle this correctly, it will crash suddenly and the user will have a very disappointing experience with your product.
But if you do handle the exception, you will be able to provide an alternative to improve the experience of the user.
Perhaps you could display a descriptive message asking the user to enter a valid input, or you could provide a default value for the input. Depending on the context, you can choose what to do when this happens, and this is the magic of error handling. It can save the day when unexpected things happen. ⭐️

What Happens Behind the Scenes?
Basically, when we handle an exception, we are telling the program what to do if the exception is raised. In that case, the "alternative" flow of execution will come to the rescue. If no exceptions are raised, the code will run as expected.

Time to Code: The try ... except Statement
Now that you know what exceptions are and why you should we handle them, we will start diving into the built-in tools that the Python languages offers for this purpose.
First, we have the most basic statement: try ... except.
Let's illustrate this with a simple example. We have this small program that asks the user to enter the name of a student to display his/her age:
students = {"Nora": 15, "Gino": 30}

Notice how we are not validating user input at the moment, so the user might enter invalid values (names that are not in the dictionary) and the consequences would be catastrophic because the program would crash if a KeyError is raised:

# User Input
Please enter the name of the student: "Daniel"

Syntax
We can handle this nicely using try ... except. This is the basic syntax:
try:
  # code
except:
  # code


Catching Specific Exceptions
Since not all types of exceptions are handled in the same way, we can specify which exceptions we would like to handle with this syntax:
try:
  # code
except <type>:
  # code

Multiple Except Clauses
To do this, we need to add multiple except clauses to handle different types of exceptions differently.
According to the Python Documentation:
A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed.
In this example, we have two except clauses. One of them handles ZeroDivisionError and the other one handles ValueError, the two types of exceptions that could be raised in this try block.

💡 Tip: You have to determine which types of exceptions might be raised in the try block to handle them appropriately.

Multiple Exceptions, One Except Clause
You can also choose to handle different types of exceptions with the same except clause.

According to the Python Documentation:
An except clause may name multiple exceptions as a parenthesized tuple.
This is an example where we catch two exceptions (ZeroDivisionError and ValueError) with the same except clause:

Handling Exceptions Raised by Functions Called in the try Clause
An interesting aspect of exception handling is that if an exception is raised in a function that was previously called in the try clause of another function and the function itself does not handle it, the caller will handle it if there is an appropriate except clause.

According to the Python Documentation:
Exception handlers don’t just handle exceptions if they occur immediately in the try clause, but also if they occur inside functions that are called (even indirectly) in the try clause.

Now Let's Add: The "else" Clause
The else clause is optional, but it's a great tool because it lets us execute code that should only run if no exceptions were raised in the try clause.
try:
  # code
except:
  # code
else:
  # code

According to the Python Documentation:
The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception.

💡 Tip: According to the Python Documentation:
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

The "finally" Clause
The finally clause is the last clause in this sequence. It is optional, but if you include it, it has to be the last clause in the sequence. The finally clause is always executed, even if an exception was raised in the try clause. 
try:
  # code
except:
  # code
else:
  # code
finally:
  # code

According to the Python Documentation:
If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception.
The finally clause is usually used to perform "clean-up" actions that should always be completed. For example, if we are working with a file in the try clause, we will always need to close the file, even if an exception was raised when we were working with the data.

❗️Important: remember that the else clause and the finally clause are optional, but if you decide to include both, the finally clause has to be the last clause in the sequence.

Raising Exceptions
Now that you know how to handle exceptions in Python, I would like to share with you this helpful tip: you can also choose when to raise exceptions in your code.
This can be helpful for certain scenarios. Let's see how you can do this:

raise ValueError("The argument must have five elements")
where 'raise' is a keyword, 'ValueError' is an Exception, and the string 'The argument must have five elements' is the message.

The output would be:
ValueError: The argument must have five elements
Notice how the last line displays the descriptive message:
ValueError: The argument must have five elements
You can then choose how to handle the exception with a try ... except statement. You could add an else clause and/or a finally clause. You can customize it to fit your needs.
"""