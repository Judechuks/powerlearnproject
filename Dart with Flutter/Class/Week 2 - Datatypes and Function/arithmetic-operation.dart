void main() {
  // declaring two numbers
  int num1 = 10;
  int num2 = 3;

  // performing arithmetic calculation
  int sum = num1 + num2; // addition
  int diff = num1 - num2; // subtraction
  int subtract = num2 - num1; // unary minus
  int mul = num1 * num2; // multiplication
  double div = num1 / num2; // division
  int div2 = num1 ~/ num2; // integer division
  int mod = num1 % num2; // show remainder

//Printing info
  print("The addition is $sum.");
  print("The subtraction is $diff.");
  print("The unary minus is $subtract");
  print("The multiplication is $mul.");
  print("The division is $div.");
  print("The integer division is $div2.");
  print("The modulus is $mod.");
}

/* OUTPUT:
The addition is 13.
The subtraction is 7.
The unary minus is -7
The multiplication is 30.
The division is 3.3333333333333335.
The integer division is 3.
The modulus is 1.
*/
