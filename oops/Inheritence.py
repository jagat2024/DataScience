class Animal: #parent class
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def display(self):
        print(f"The Name of the animal is {self.name} and weight of the animal is {self.weight}")
class Human(Animal):#child class
    def __init__(self, name, weight,height,age):
        super().__init__(name,weight)
        self.height=height
        self.age=age
    def display(self):
        print(f"the name of the human is {self.name},weight is {self.weight},height is {self.height},age is {self.age}")
h1=Human("jagat","73Kg",5.9,22)
h1.display()



# different forms of inheritence 

class main_factory: #grandparent class
    def __init__(self,package,zip):
        self.package=package
        self.zip=zip
    def display1(self):
        print(f"The main factory genrates {self.package} and {self.zip}")
class Production_factory(main_factory): 
    def __init__(self,package,zip,raincover):
        super().__init__(package,zip)
        self.raincover=raincover
    def display1(self):
        print(f"The main factory genrates {self.package} and {self.zip} and also {self.raincover}")
class final(Production_factory):
    def __init__(self,package,zip,raincover,bag):
        super().__init__(package,zip,raincover)
        self.bag=bag
    def display(self):
        print(f"The final product  by using {self.package},{self.zip},{self.raincover}={self.bag}")
s1=final("rainreplent","highquality zip","urabnfynix raincover", "Safari bags")
s1.display()