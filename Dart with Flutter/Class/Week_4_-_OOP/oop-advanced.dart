/*
An object-oriented model that uses classes and inheritance
A class that implements an interface
A class that overrides an inherited method
An instance of a class that is initialized with data from a file
A method that demonstrates the use of a loop
*/

import 'dart:io';

// Define an abstract class 'Animal' with a method 'makeSound'
abstract class Animal {
  void makeSound();
}

// Create a class 'Dog' that implements the 'Animal' interface
class Dog implements Animal {
  @override
  void makeSound() {
    print('Dog barks!');
  }
}

// Create a class 'Cat' that extends 'Animal'
class Cat extends Animal {
  @override
  void makeSound() {
    print('Cat meows!');
  }
}

// Create a class 'Zoo' that initializes animals from a file
class Zoo {
  List<Animal> animals = [];

  Zoo(String filePath) {
    final file = File(filePath);
    final lines = file.readAsLinesSync();

    for (var line in lines) {
      if (line.toLowerCase() == 'dog') {
        animals.add(Dog());
      } else if (line.toLowerCase() == 'cat') {
        animals.add(Cat());
      }
    }
  }

  void displayAnimalSounds() {
    for (var animal in animals) {
      animal.makeSound();
    }
  }
}

void main() {
  // Initialize a Zoo with data from a file (e.g., "animals.txt")
  final zoo = Zoo('animals.txt');

  // Demonstrate animal sounds
  zoo.displayAnimalSounds();

  // Example of a loop (printing numbers from 1 to 5)
  for (var i = 1; i <= 5; i++) {
    print('Loop iteration $i');
  }
}
/* *From Co-pilot*
In this program:

We define an abstract class Animal with a method makeSound.
The Dog class implements the Animal interface, and the Cat class extends Animal.
The Zoo class reads animal names from a file (e.g., “animals.txt”) and initializes instances of Dog and Cat.
The displayAnimalSounds method prints the sounds made by each animal.
Lastly, we demonstrate the use of a loop to print numbers from 1 to 5.
Remember to replace "animals.txt" with the actual path to your data file containing animal names (one per line). 🐶🐱
*/
