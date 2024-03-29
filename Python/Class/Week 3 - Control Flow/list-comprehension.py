nums = [4, -11, 69, 53, -65]
doubled = []

for num in nums:
  doubled.append(num * 2)

print("longer method", doubled)

# shorter way
nums = [4, -11, 69, 53, -65]
doubled = [num * 2 for num in nums]
print("shorter method", doubled)

# General syntax of list comprehension looks like this:
# new_list = [<expression> for <element> in <collection>]