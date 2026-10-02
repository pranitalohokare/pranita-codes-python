#del keyword
'''
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Pranita")
print(s1.name)
del s1.name
print(s1.name)  # This will raise an AttributeError since 'name' has been deleted

#Private attributes and methods(private members are not accessible outside the class)
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private attribute

    def display_pass(self):
        print("Account password:", self.__acc_pass)

acc1 = Account("12345", "mysecretpass")
print(acc1.acc_no)  # Accessible
#print(acc1.__acc_pass) This will raise an AttributeError since '__acc_pass' is private
acc1.display_pass() #this will print the password because it is a method of the class and can access private attributes
'''
#private methods
class person:
    __name = "Pranita"  # private attribute

    def __hello(self): # private method
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()
p1.welcome()  # This will call the private method through a public method
