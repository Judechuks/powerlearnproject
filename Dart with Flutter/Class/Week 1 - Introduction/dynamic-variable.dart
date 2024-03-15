void main() {
  dynamic x = 12; // type: integer
  x = "Hello world"; // type: string
  x = false; // type: boolean
  print(x);
}

/*
Output:
false

NOTE: the value was change from "Hello world" (which is a String datatype) to false (which is a bool datatype). Ordinarily this is not allowed in dart. but it is possible because it is a dynamic variable
*/
