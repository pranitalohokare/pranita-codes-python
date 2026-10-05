# Single inheritance(one base class and one derived class)
class Car:
    @staticmethod   
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")

class ToyotaCar(Car):
    def __init__(self, model):
        self.model = model

car1 = ToyotaCar("Camry")
car2 = ToyotaCar("Fortuner")

print(car1.model)  # Output: Camry
print(car2.model)  # Output: Fortuner
print(car1.start())  # Output: Car is starting...

# multilevel inheritance(one class is derived from base class and another class is derived from the derived class ...)

class Car:
    @staticmethod
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")

class ToyotaCar(Car):
    def __init__(self, model):
        self.model = model

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("4x4")
print(car1.type)  # Output: 4x4
car1.start()  # Output: Car is starting...

#multiple inheritance(two base classes and one derived class)

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varA)  # Output: welcome to class A
print(c1.varB)  # Output: welcome to class B
print(c1.varC)  # Output: welcome to class C

#Super Method (super() method is used to call the constructor of the parent class)
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod   
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")

class ToyotaCar(Car):
    def __init__(self, model, type):
        self.model = model
        super().__init__(type) # calling the constructor of the parent class
        super().start() # calling the start method of the parent class

car1 = ToyotaCar("Camry", "electrical")
print(car1.type)
