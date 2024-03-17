void main() {
  List<String> names = ["John", "James", "Peter"];
  print("Values of names is $names");
  print("Values of names[0] is ${names[0]}"); // index 0
  print("Values of names[1] is ${names[1]}"); // index 1
  print("Values of names[2] is ${names[2]}"); // index 2
  print(names);
  /* NOTE:
    You can add a list of different datatypes as seen below:
  */
  List<dynamic> mixedList = [1, "PowerLearnProject", true, 10.5, "\u{1F600}"];
  print(mixedList);
}
