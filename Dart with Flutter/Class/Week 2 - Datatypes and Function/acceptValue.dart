// import the input output from the standard library
import 'dart:io';

void main() {
  print("What is your name?");
  String name = stdin.readLineSync()!;
  print("Welcome $name");

  int addTwo() {
    print("Enter first Number: ");
    // read the text from the standard input stream and stores the value into the variable num1
    int num1 = int.parse(stdin.readLineSync()!);
    print("Enter second Number: ");
    int num2 = int.parse(stdin.readLineSync()!);
    return num1 + num2;
  }

  print("Total: ${addTwo()}");
}
