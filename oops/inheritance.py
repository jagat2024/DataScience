#create a  class electric car  that inheritance from the car class and has and other attrubute as batery cisze
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand}{self.model}"
class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
my_car=Electric_car("tesla","s","85kwh")
print(my_car.model)
print(my_car.fullname())