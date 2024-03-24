# empty list
my_list = []

# appending values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# updating list
my_list[1] = 15
print(my_list)

# extending list
my_list.extend([50, 60, 70])
print(my_list)

# removing last element
my_list.pop()
print(my_list)

# sorting in ascending order
my_list.sort( reverse=False)
print("Index of 30 is:", my_list.index(30))
