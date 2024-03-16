void main() {
  // int used to store age as whole numbers
  String name = "Monye Jude"; // String
  int age = 20; // int
  bool isMarried = false; // bool
  num yearsOfExperience; // num and null
  yearsOfExperience = 0; // num
  List<String> language = ["C++", "Java", "Javascript"]; // List
  Map<String, int> progress = {
    "Database": 50,
    "Dart": 20,
    "Web Dev": 50
  }; // Map

  print(
      "My name is $name I'm $age years old. I have $yearsOfExperience years of experience in programming.");
  print("My favorite programming languages are: $language");
  print("Married?: $isMarried");
  print("My progress so far in LMS is: $progress");
  print("I'm happy \u{1F600} to be part of PLP Academy"); // runes
}
