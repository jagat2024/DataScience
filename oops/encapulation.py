class Car():
    def __init__(self, model, brand):
        self.__brand = brand   # private attribute
        self.model = model

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



'''encapsulation point 2'''
class Demo:
    def __init__(self,name,age,salary):
        self.name=name
        self._age=age
        self.__salary=salary
    def show(self):
        print("public: ",self.name)
        print("Protected: ",self._age)
        print("private: ",self.__salary)
obj=Demo("Jagat",22,75000)
obj.show()
obj.__salary#it will give an error as no attribute has name __salary dince when we call it take it as _demo.__salary which is not there

        