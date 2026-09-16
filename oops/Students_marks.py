class Students:
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def Total(self):
        return self.marks1+self.marks2+self.marks3
    def average(self):
        return self.Total()/3
    def result(self):
        print(f"The total marks of the student is {self.Total()} and average of the student is {self.average()}")
        if(self.average()>=40):
            print("PASS")
        else:
            print("FAIL")
s1=Students(56,67,89)
s1.result()

    