/*
Create a program that has the following features:
An object-oriented model that uses classes and inheritance
A class that implements an interface
A class that overrides an inherited method
An instance of a class that is initialized with data from a file
A method that demonstrates the use of a loop
*/
import 'dart:io';

// Defining an abstract class 'Human' with a method 'grow'
abstract class Human {
  void grow(); // method
}

// creating a class 'Man' that implements the 'Human' interface
class Man implements Human {
  @override
  void grow() {
    print("Man: increase in height and Muscle");
  }
}

// creating a class 'Woman' that extends 'Human'
class Woman extends Human {
  @override
  void grow() {
    print("Woman: Change in body shape and curves");
  }
}

// creating a class 'Family' that initializes Humans from a file
class Family {
  List<Human> familyMembers = [];

  // constructor
  Family(String filePath) {
    final file = File(filePath);
    final lines = file.readAsLinesSync();

    // looping through the file
    for (var line in lines) {
      if (line.toLowerCase() == 'man') {
        familyMembers.add(Man());
      } else if (line.toLowerCase() == 'woman') {
        familyMembers.add(Woman());
      }
    }
  }

  // a method that demonstrates the use of a loop to call the grow method for all familyMembers
  void displayFamilyMembersGrowth() {
    for (var familyMember in familyMembers) {
      familyMember.grow();
    }
  }
}

void main() {
  // Initializing An example of family with data from an external file (e.g. 'familyFile.txt')
  final family = Family('familyFile.txt');
  family.displayFamilyMembersGrowth();
}
