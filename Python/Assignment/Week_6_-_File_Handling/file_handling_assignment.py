# 4. implementing try...catch
try:
  # 1. Open a new text file named "my_file.txt" in write mode ('w')
  with open('my_file.txt', 'w') as file: # same as this code:  file = open('my_file.txt', 'w')
      # Write three lines of text to the file
      file.write('Hello, World! This is the first line.\n')
      file.write('The second line has a number: 42.\n')
      file.write('And the third line says goodbye.\n')

  print("File 'my_file.txt' has been created and written to successfully.")

  # 2. reading and displaying file
  file = open('my_file.txt', 'r')
  # reading the content of the file
  content = file.read()
  # displaying the content of the file
  print('The content of my_file.txt file:')
  print(content)

  # 3. appending content to the file
  file = open('my_file.txt', 'a')
  # Append three additional lines of text to the existing content
  file.write('Appending this fourth line.\n')
  file.write('Followed bt this line.\n')
  file.write('And then lastly this line of text.\n')

except FileNotFoundError:
  print("Error: 'my_file.txt' does not exist. Please check the file name and try again.")
except PermissionError:
  print("Error: You do not have the necessary permissions to read or write to 'my_file.txt'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")
finally:
  print("File operations are complete.")