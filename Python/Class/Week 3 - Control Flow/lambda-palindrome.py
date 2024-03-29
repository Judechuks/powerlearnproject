"""
Define a function that determines whether a given string is a Palindrome. 
NB: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or omo
"""
# Palindrome without lambda
def isPalindrome(string):
  if (string == string[::-1]):
    return "A Palindrome"
  else:
    return "Not a Palindrome"
# Enter input string
string = input("Enter string: ")
# call the function and pass input from the user - string variable
print(f"{string} = {isPalindrome(string)}")

# Palindrome with lambda
lambdaPalindrome = lambda string : "Palindrome" if string == string[::-1] else "Not Palindrome"
string = input("Enter string: ")
# call the function and pass input from the user - string variable
print(f"{string} = {lambdaPalindrome(string)}")