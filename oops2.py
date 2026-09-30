#four pillars of OOPS - encapsulation, inheritance, polymorphism, abstraction
#encapsulation = wrapping data and functions into a single unit. (creating class and defining attributes and methods inside it and creating object of class to access attributes and methods is called encapsulation)
#abstraction = hiding the implementation details of a class and showing only the essential features to the user.
class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("car started")

car1 = Car()
car1.start()

#create account class with 2 attributes - balance & account no. create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Debited amount: Rs.", amount)
        else:
            print("Insufficient balance")

    def credit(self, amount):
        self.balance += amount
        print("Credited amount: Rs.", amount)

    def print_balance(self):
        print("Balance: Rs.", self.balance)

A1 = Account(1000, 12345)
A1.debit(500)
A1.print_balance()
A1.credit(200)
A1.print_balance()
