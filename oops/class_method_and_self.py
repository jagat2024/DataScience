#add a method to the car class that display the full name of the car (brand and model)
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand}{self.model}"
mycar=Car("honda","2016")
print(mycar.model)
print(mycar.fullname())
    