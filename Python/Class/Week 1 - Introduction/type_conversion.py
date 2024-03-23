# 1. Implicit type conversion
a = 10
b = 20.5
c = a + b
print("c =", c, "and is a type of", type(c))

# 2. Explicit type conversion
# int() float() str()
new_a = float(a)
new_b = int(b)
new_c = str(new_a + new_b)
d = "new_a + new_b = " + new_c

print("After explicit conversion a = ", new_a, "and is a type of", type(new_a))
print("After explicit conversion b = ", new_b, "and is a type of", type(new_b))
print("After explicit conversion c = ", new_c, "and is a type of", type(new_c))
print(d)

# print parameters
print("Hi!", "my name", "is", "Jude", sep="_ ", end="\n")