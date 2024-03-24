# set: are list of unique items i.e it does not accept duplicate values. It is enclosed in a curly bracket.
# The items in a set have no orderly arrangement i.e their order of arrange varries

# Initializing a set
emptySet = set()

# Initializing a dictionary
emptyDictionary = {}

# set examples
Ids = {110, 111, 112, 113, 114, 115, 116, 117, 118}
print("IDs:", Ids)

# in the case of duplicate values, python removes the duplicates
Ids = {110, 111, 112, 113, 114, 115, 116, 117, 118, 112, 110, 111}
print("Unique IDs:", Ids)

# add(): Add method adds an item to a set
Ids.add(119)
print("IDs:", Ids)

# update(): Update method updates/adds an item to a set
newIds = {120, 121, 122, 123, 124}
Ids.update(newIds)
print("Updated IDs:", Ids)

# discard(item): Discards/removes an item from a set
Ids.discard(124)
print("IDs after discarding:", Ids)

# remove(item): Removes an item from a set
Ids.remove(123)
print("IDs after removing:", Ids)

# pop(): Removes the last item in the set
# clear(): Removes all the items in the set
# update(): Adds element to the set
# all(): Returns True if all the elements of the set are true (or if the set is empty)
# any(): Returns True if any of the elements of the set are true (if the set is empty it returns False)
# enumerate(): To list out all the element in the set
# len(): To get the number of items in a set
# max(): Returns the largest item in the set
# min(): Returns the smallest item in the set
# sorted(): Returns a new sorted list from elements in the set (does not sort the set itself)
# sum(): Returns the sum of all the elements in the set
# difference():	Returns a set that is the difference between two sets
# copy():	Returns a shallow copy of the set

# Operations in set 
# Union: combining the elements of one set to another
A = {1, 3, 5}
B = {0, 2, 4}
# 1. Union operation using |
print("Union using |:", A | B) # output: {0, 1, 2, 3, 4}
# union operation using union() method
print("Union using union():", A.union(B)) # output: {0, 1, 2, 3, 4}

# 2. Intersection: elements that are common in a set and another set or sets
C = {2, 4, 6}  
# intersection operation using &
print("Union using &:", B & C) # output: {2, 4}
# intersection operation using intersection() method
print("Union using intersection():", B.intersection(C)) # output: {2, 4}

# 3. Difference between two sets: elements of setA that are not present in setB
# C = {2, 4, 6}  
# difference operation using -
print("Union using - between A and C:", A - C) # output: {1, 3, 5}
print("Union using - between C and A:", C - A) # output: {2, 4, 6}
# difference operation using difference() method
print("Union using difference() between A and C:", A.difference(C)) # output: {1, 3, 5}
print("Union using difference() between C and A:", C.difference(A)) # output: {2, 4, 6}

# 4. Symmetric Difference between two sets: elements that are not common between two sets (disjoints)
# C = {2, 4, 6}  
# difference operation using ^
print("Union using - between A and C:", A ^ C) # output: {1, 2, 3, 4, 5, 6}
print("Union using - between C and A:", C ^ A) # output: {1, 2, 3, 4, 5, 6}
# difference operation using symmetric_difference() method
print("Union using symmetric_difference() between A and C:", A.symmetric_difference(C)) # output: {1, 2, 3, 4, 5, 6}
print("Union using symmetric_difference() between C and A:", C.symmetric_difference(A)) # output: {1, 2, 3, 4, 5, 6}

# equal: to check is two sets are equal using ==
D = {4, 6, 2} 
if A == C:
  print("SetA is equal to SetC")
else:
  print("SetA is not equal to SetC")

if D == C:
  print("SetD is equal to SetC")
else:
  print("SetD is not equal to SetC")
