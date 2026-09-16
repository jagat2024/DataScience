class Animal:
    def show(self):
        print("this is animal class")
class Human:
    def show(self):
        print("this is human class")
ob1=Animal()
ob2=Human()
ob1.show() # show is same instance in both animal and human class but each have diff output what we term as polymorphism
ob2.show() # show is same instance in both animal and human class but each have diff output what we term as polymorphism