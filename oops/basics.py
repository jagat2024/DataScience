#create a car class with attribute and models then create an instance in the class 
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
My_car=Car("toyota","corolla")
print(My_car.brand,My_car.model)
