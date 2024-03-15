class Employee {
  static var emp_dept;
  var emp_name;
  int emp_salary = 0;

  void showDetails() {
    print("Name of the Employee is: $emp_name");
    print("Salary of the Employee is: $emp_salary");
    print("Dept. of the Employee is: $emp_dept");
  }
}

void main() {
  Employee e1 = Employee();
  Employee e2 = Employee();

  Employee.emp_dept = "MIS";

  e1.emp_name = 'Rahul';
  e1.emp_salary = 50000;
  e1.showDetails();

  e2.emp_name = 'Tina';
  e2.emp_salary = 55000;
  e2.showDetails();
}
/*
Output:
Name of the Employee is: Rahul
Salary of the Employee is: 50000
Dept. of the Employee is: MIS
Name of the Employee is: Tina
Salary of the Employee is: 55000
Dept. of the Employee is: MIS

NOTE: The two employee gets the same department. If you want to change that then use:
Employee.emp_dept = "ICT";
after the assignmnent for the second employee, let say after line 24( before line 25)
*/

