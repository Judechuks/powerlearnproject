# append(): adds a value at the end of a list
numbers = [1,2,3,4]
print("Before append", numbers)
numbers.append(5)
print("after append", numbers)

# extend(): We use the extend() method to add all items of one list to another.
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
odd_numbers.extend(even_numbers)
print(odd_numbers)

# mutating: we can mutate a list by assigning a value to an index
odd_numbers[5] = 11
print(odd_numbers)

# len(item): is used to know the length of items in a list
print("Length of number:", len(numbers))

# del: In Python, we can use the del statement to remove one or more items from a list. And to delete a variable
languages = ["Python", "Swift", "C++", "C", "Java", "Rust", "R"]
del languages[6]
print(languages)

# remove(item): We can also use the remove() method to delete a list item.
languages.remove("C")
print(languages)

# insert(index, item): inserts an item to a list at a specified index 
languages.insert(2, "Dart")
print("Languages after insertion:", languages)

# pop(index): returns and remove items present at a given index 
numbers.pop(4)

# clear(): iremoves all items from the list 
numbers.clear()
print("numbers cleared:", numbers)

# index(): returns the index of the first matched item 
print("Index of C++:", languages.index("C++"))

# count(): returns the number of times the specified item appeared in a list
randomNumber = [1, 5, 6, 5, 8, 7, 5, 3, 2, 9, 4, 5, 0]
print("Count:", randomNumber.count(5))

# sort(): sorts the list in an ascending/descending order 
languages.sort(reverse=True)
print("Languages sorted:", languages)

# reverse(): reverses the item of a list
languages.reverse()
print("Languages reversed:", languages)

# copy(): returns the shallow copy of the list
copiedLanguages = languages.copy()
print("Copied Languages", copiedLanguages)

# iterating a list using for-in
for language in languages:
  print(language)

"""
Python List Comprehension
List comprehension is a concise and elegant way to create lists.
A list comprehension consists of an expression followed by the for statement inside square brackets.
"""
myNumbers = [myNumber*myNumber for myNumber in range(1,6)]
print(myNumbers) # output: [1, 4, 9, 16, 25]
# Here is an example to make a list with each item being increasing by power of 2.