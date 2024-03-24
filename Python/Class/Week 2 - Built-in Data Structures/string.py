# f-String allows one to interpolate (i.e use variables in strings)
name = 'Jude' # single quote
country = 'UK' # double quote
message = """Hello and welcome!"""
docStringMessage = """
Nice meeting you!
"""

print(f'{name} from {country}') # output: Jude from UK
print(f'{name} from {country}, {message}') # output appears in straight line
print(f'{name} from {country}, {docStringMessage}') # output appears in different line as written

# indexing
print("Indexing", name[0]) # output: J

# negative indexing
print("Negative Indexing:", name[-3]) # output: ud

# slice using [:]
print("Slice:", name[1:3]) # output: ud

#Membership in strings
# in (same as in dictionary)
# not in (same as in dictionary)

# methods 
# len(): the number of characters that make up the string (including spaces)
# del: to delete a character
# index(): to get the index of a character in a string
# count(): to number of times a character appeared in a string
print(f'Count: {message.count("l")}') # Output: 3

# startswith(): returns True if a particular character starts the string or False if otherwise
print(message.startswith("H")) # Output: True

# split(): splits string by words into a list starting from left
splited = (message.split())
print(splited) # Output: ['Hello', 'and', 'welcome!']

# rstrip(): Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry and mango"
x = txt.rsplit(", ")
print(x) # Output: ['apple', 'banana', 'cherry']

# rstrip():
txt = " banana "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# upper() turns a string into uppercase
print(message.upper())

# lower(): turns a string into lowercase
print(message.lower())

# partition() 
# replace() 
# find() 
# isnumeric() 