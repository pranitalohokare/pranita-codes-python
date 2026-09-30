#to map with real world scenarios, we started using OOPS concepts in python
#classes and objects (class is a blueprint, object is an instance of class)
'''
class Student:
    name = "karan"

s1 = Student() #creating object of class Student
print(s1.name) #accessing attribute of class using object

class Car:
    color = "red"
    model = "BMW"
    year = 2020
c1 = Car()
print(c1.color)
print(c1.model)
print(c1.year)

#__init__function (constructor) - it is a special function that is called when an object of class is created
class Person:
    def __init__(self, name, marks): #the self parameter is a reference to the current instance of the class
        self.name = name
        self.marks = marks
        print("object is created")
p1 = Person("Pranita", 100) #object is created
print(p1.name)
print(p1.marks)
p2 = Person("Panu", 90)
print(p2.name)
print(p2.marks)

#methods in class(functions inside class that belongs to objects of that class)
class student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome", self.name, "to", student.college_name)

    def get_marks(self):
        return self.marks
    
s1 = student("pranita", 100)
s1.welcome()
print(s1.get_marks())

class Student:
    def __init__(self, name, marks1, marks2, marks3): #can also make list of marks instead of 3 parameters(just assign marks parameter here and give 3 valuess in list, in the object)
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def avg(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3 #can do a loop if have more number of marks
        return avg
s1 = Student("pranita", 90, 80, 90)
print("average of pranita: ", s1.avg())
s2 = Student("sarthak", 70, 60 , 100)
print("average of sarthak: ", s2.avg())
s3 = Student("kalpana", 100, 90, 90)
print("average of kalpana: ", s3.avg())

#static methods - they are methods that belong to the class rather than the object of the class, they can be called without creating an object of the class
class Math:
    @staticmethod #decorator to define static method
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
print(Math.add(10, 5)) #calling static method without creating object of class
print(Math.subtract(10, 5))
'''