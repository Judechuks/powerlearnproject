names = ["Jude", "John", "James", "Janet", "Josephine" ]

# for in
for name in names:
  print(name)

# for loop using range 
five_steps = range(5) # 1, 2, 3, 4, 5
msg = "Welcome!"
for i in range(5):
  print(msg)

# while loop
count = 0
while count <= 2:
  print(count)
  count += 1

# loop controls: break and continue
# break: The break statement is used to terminate the loop immediately when it is encountered.
count = 0
while count < len(names):
  print(names[count])
  if(names[count] == "James"):
    print("Oopss!")
    break
  count += 1

# continue: The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.
ages = [23, 18, 20, 26]
for age in ages:
  if age < 21:
    continue
  print(age)

# Nested Loops:In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over
continents = [["Japan", "China", "Korea"], ["Spain", "Portugal", "France"], ["Nigeria", "Ghana", "Kenya"]]
for continent in continents:
  print(continent)
  for country in continent:
    print(country)