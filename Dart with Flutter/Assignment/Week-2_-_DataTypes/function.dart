int addTwo(int num1, int num2) {
  return num1 + num2;
}

int subtractTwo(int num1, int num2) {
  return num1 - num2;
}

int multiplyTwo(int num1, int num2) {
  return num1 * num2;
}

double divideTwo(int num1, int num2) {
  return num1 / num2;
}

int stringLength(String word) {
  return word.length;
}

String getFirstElement(List listOfItems) {
  return listOfItems[0];
}

void main() {
  int num1 = 30;
  int num2 = 10;
  int total = addTwo(num1, num2);
  String string1 = "Jude";
  List myList = ["Apple", "Mango", "Pineapple", "Orange"];
  print("$num1 + $num2 = $total");
  print("$num1 - $num2 = ${subtractTwo(num1, num2)}");
  print("$num1 x $num2 = ${multiplyTwo(num1, num2)}");
  print("$num1 / $num2 = ${divideTwo(num1, num2)}");
  print("The length of the word $string1 = ${stringLength(string1)}");
  print("The first item in the $myList is ${getFirstElement(myList)}");
}
