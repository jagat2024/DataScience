'''Q5. Employee Salary

Create:

class Employee:

Attributes:

name
salary

Method:

annual_salary()

Create 3 employees and print their annual salaries.

Then find the employee having the highest salary.'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Annual_salary(self):
        An_sal=self.salary*12
        return An_sal
    def DISPLAY(self):
        print(f"The annual salary of the employee is {self.Annual_salary()} with an bonus of {self.Annual_salary()*0.51}")
e1=Employee("Sagnik",40000)
e1.Annual_salary();
e1.DISPLAY();
