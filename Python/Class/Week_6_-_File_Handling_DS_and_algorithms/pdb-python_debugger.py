"""
1. Python’s interactive source code debugger.
"""
# import pdb; pdb.set_trace()

"""
2. Starting in Python 3.7, there’s another way to enter the debugger. PEP 553 describes the built-in function breakpoint(), which makes entering the debugger easy and consistent:
"""
# breakpoint()
"""
By default, breakpoint() will import pdb and call pdb.set_trace(), as shown above. However, using breakpoint() is more flexible and allows you to control debugging behavior via its API and use of the environment variable PYTHONBREAKPOINT.

For example, setting PYTHONBREAKPOINT=0 in your environment will completely disable breakpoint(), thus disabling debugging. If you’re using Python 3.7 or later, I encourage you to use breakpoint() instead of pdb.set_trace().
You can also break into the debugger, without modifying the source and using pdb.set_trace() or breakpoint(), by running Python directly from the command-line and passing the option -m pdb. If your application accepts command-line arguments(https://realpython.com/python-command-line-arguments/), pass them as you normally would after the filename. For example:
"""
# python3 -m pdb app.py arg1 arg2
"""
There are a lot of pdb commands available. At the end of this tutorial, there is a list of Essential pdb Commands(https://realpython.com/python-debugging-pdb/#essential-pdb-commands). For now, let’s use the p command to print a variable’s value. Enter p variable_name at the (Pdb) prompt to print its value.
Let’s look at the example. Here’s the example1.py source:
"""
#!/usr/bin/env python3
filename = __file__
import pdb; pdb.set_trace()
print(f"path= {filename}")

"""
Since you’re in a shell and using a CLI (command-line interface), pay attention to the characters and formatting. They’ll give you the context you need:

  > starts the 1st line and tells you which source file you’re in. After the filename, there is the current line number in parentheses. Next is the name of the function. In this example, since we’re not paused inside a function and at module level, we see <module>().
  -> starts the 2nd line and is the current source line where Python is paused. This line hasn’t been executed yet. In this example, this is line 5 in example1.py, from the > line above.
  (Pdb) is pdb’s prompt. It’s waiting for a command.

Use the command q to quit debugging and exit.

These are the basic commands that you can use with pdb to debug your code. There are many more advanced commands available that can help you better understand and diagnose bugs in your code. To learn more about pdb and its commands, you can refer to the official Python documentation
"""