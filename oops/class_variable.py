# add a class variable to car that keeps track of the number of cars created
class Car():
    total_car=0
    def __init__(self, model, brand):
        self.__brand = brand   # private attribute
        self.model = model
        Car.total_car+=1

    def get_brand(self):      # getter method
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
class Electric_car(Car):
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)   # correct order
        self.battery_size = battery_size

    def full_name(self):
        return f"{self.get_brand()} {self.model} {self.battery_size}"
my_car = Car("swift", "maruti")
elec = Electric_car("tesla", "b6", "85kwh")
print(my_car.full_name())
print(elec.full_name())
print(Car.total_car)