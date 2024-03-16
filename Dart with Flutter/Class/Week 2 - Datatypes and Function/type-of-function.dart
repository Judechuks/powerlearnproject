// parameter and return type
int add(int a, int b) {
  var total;
  total = a + b;
  return total;
}

// parameter and no return type
void mul(int a, int b) {
  var total;
  total = a * b;
  print("Multiplication is : $total");
}

// no parameter and return type
String greet() {
  String greet = "Welcome";
  return greet;
}

// no parameter and no return type
void greetings() {
  print("Hello World!!!");
}

void main() {
  var total = add(2, 3);
  print("Total sum: $total");
  mul(2, 3);
  var greeting = greet();
  print("Greeting: $greeting");
  greetings();
}
/*
OUTPUT:
Total sum: 5
Multiplication is : 6
Greeting: Welcome
Hello World!!!

NOTE:
void details(@required String name){ 
  print(name)
// the @required denotes that a value must be passed in the function call
}

void details([String name]){ 
  print(name)
// the [] denotes that passing the value is optional in the function call
}

void details([String name = "John"]){ 
  print(name)
// you can pass a default value to a parameter
}

*/ 
