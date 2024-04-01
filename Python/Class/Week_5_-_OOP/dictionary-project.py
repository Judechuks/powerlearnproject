"""
TASK: create a program that automates searching for a word definition in a dictionary.
We should have a data source (dictionary-data/data.json)
Learn how to load json data into a python dictionary
Create a function that returns a definition of a word
Consider a condition that the entered word is not in a dictionary
Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here
"""
"""
STEPS
1. Data Source:
First, you need a data source containing word definitions. If you have a JSON file with word definitions, we can use that.
2. Load JSON Data into a Python Dictionary:
Load the data from the JSON file into a Python dictionary. You can use the json module for this.
Assume the dictionary data is stored in a file named “dictionary.json”.
3. Create a Function to Get Word Definitions:
Write a function that takes a word as input and returns its definition.
Handle different cases (upper/lower/mixed) by converting the input word to lowercase.
Check if the word exists in the dictionary. If yes, return its definition.
If not, use the difflib library to find close matches and suggest the closest match to the user.
Here’s a high-level implementation of the steps above:
"""

import json
from difflib import get_close_matches

# load the dictionary data from the provided JSON file
def load_dictionary(file_path):
  with open(file_path, 'r') as file: # 'r' = read
    return json.load(file)
  
# create a function that returns the definition of a word
def get_definition(word, data):
  word = word.lower() # converts the user's input to a lowercase letter to handle different cases
  if word in data: # checking if the word exists
    return data[word]
  elif word.title() in data: # If user entered "texas", this will check for Texas as well. title() is used to capitalize a sentence or statement
    return data[word.title()]
  elif word.upper() in data: # incase user enters words like NATO, USA, etc
    return data[word.upper()]
  else: # find close matches to the entered word
    close_matches = get_close_matches(word, data.keys())
    if close_matches:
      # suggest the closest match to the user
      suggestion = close_matches[0]
      return f"Did you mean {suggestion}? If yes, the definition is: {data[suggestion]}"
    else:
      return "The word does not exist in the dictionary."
    
dictionary_data = load_dictionary("dictionary-data/data.json")

# Get input from the user
user_input = input("Enter a word to get its definition: ")

# Get the definition of the word entered by the user
definition = get_definition(user_input, dictionary_data)

# Print the definition or suggestion
print(definition)