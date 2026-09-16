class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    print("====================SUCCESSFULLY IMPORTED IN STUDENT CLASS==========================")

s1=Student("jagat",22,"CSE")
print(s1.age,s1.name,s1.branch)
s2=Student("Sagnik",21,"Mathematics and Computing")
print(s2.age,s2.name,s2.branch)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
R1=Rectangle(12,13)
print(R1.area())
print(R1.perimeter())