# Python dictionary is an ordered collection (starting from Python 3.7) of items. It stores elements in key/value pairs. Here, keys are unique identifiers that are associated with each value.

countries = {"Nigeria": "Abuja", "Ghana": "Accra", "Kenya": "Nairobi"}
print(countries["Nigeria"])

"""
In the above example, we have created a dictionary named countries. Here,
The Keys are "Nigeria", "Ghana", "Kenya"
The Values are "Abuja", "Accra", "Nairobi"
Note: Here, keys and values both are of string type. We can also have keys and values of different data types.
"""

numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers[1])

# adding a new item
numbers[4] = "Four" 
print(numbers)

# Other method 
# They are used in a similar way to set and tuple 

# clear(): Removes all the items in the dictionary
# all(): Returns True if all the elements of the dictionary are true (or if the dictionary is empty)
# any(): Returns True if any of the elements of the dictionary are true (if the dictionary is empty it returns False)
# len(): To get the number of items in a dictionary
# sorted(): Returns a new sorted list from elements in the dictionary
# keys(): Returns a new object of the dictionary's keys
print(countries.keys())

# values():	Returns a new object of the dictionary's values
print(countries.values())

# del: To remove an item in a dictionary
del numbers[4]
print(numbers)


# Dictionary Membership Test
# We can test if a key is in a dictionary or by using the keyword in. Notice that the membership test is only for the keys and not for the values.

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# in (done using keys)
print(1 in squares) # output: True
# not in (done using keys)
print(2 not in squares) # output: True
# (done using values)
print(49 in squares) # output: False

# Iterating through a dictionary
for i in squares:
  print(squares[i])

print(all(squares)) # Output: True