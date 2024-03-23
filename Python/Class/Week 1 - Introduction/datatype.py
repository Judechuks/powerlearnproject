# python is is dynamically typed meaning you don't explicitly declare the datatype of a variable, and variable is inferred-type, its datatype is determined by its value, i.e it is implicitly decided based on the value that the variable holds.

# 1. numeric datatype (int, float, complex numbers)
# use type() to determine the datatype of a variable
num1, num2, num3 = 5, 2.0, 1+2j
print("num1 =", num1, "is a type:", type(num1))
print("num2 =", num2, "is a type:", type(num2))
print("num3 =", num3, "is a type:", type(num3))

# 2. list is an ordered collection of similar/different type of items separated by commas and enclosed within a square bracket []
languages = ["Swift", "Java", "Python", "Dart", "Kotlin", "C"]
languages [5] = "C++"
print("Examples of programming languages:", languages)
print("First language in our list is:", languages[0])

# 3. tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified
product = ("Xbox", "PES", "Console")
# product[0] = "Gameboy" # gives an error (because it is immutable)

# 4. String is a sequence of characters enclose in a single or double quote
name = "Jude"
print("My name is", name)

# 5. The Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }.
studentID = {110, 111, 112, 113, 114}
print(studentID)

# 6. Dictionary is an ordered collection of items. It stores elements in key/value pairs. Here, keys are unique identifiers that are associated with each value.
countries = {"Nigeria": "Abuja", "Ghana": "Accra", "Kenya": "Nairobi"}
print(countries["Nigeria"])


x = {}
x[2] = 10
x[1] = [20, 30, 40]
print(x[1][2])
print(x)