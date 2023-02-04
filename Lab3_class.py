# #Class//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# #1///////////////////////////
# class strupp():
#     def __init__(self):
#         self.str1 = ""
#
#     def getString(self):
#         self.str1 = input()
#     def printString(self):
#         print(self.str1.upper())
# str1 = strupp()
# str1.getString()
# str1.printString()
#2//////////////////////////
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
# class Square(Shape):
#     def __init__(self, length = 0):
#         Shape.__init__(self)
#         self.length = length
#     def area(self):
#         return self.length**2
#
# a = Square(int(input("Введите длину края фигуры: ")))
# print(a.area())
# print(Square().area())

#3///////////////////////////////////
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

Area = Rectangle(int(input("Введите длину прямоугольника: ")),int(input("Введите ширину прямоугольника: ")))
print("Площадь прямоугольника: " + str(Area.area()))

#5////////////////////////////
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
    def withdraw(self, wit):
        self.balance -= wit
        print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
print("Please, write your name and balance. Press 'enter' to continue...")
own = Account(input("Account owner's name: "), int(input("Balance: ")))
str1 = input("Write Withdraw or Deposit: ")
if str1 == "Withdraw":
    own.withdraw(int(input("Write the amount: ")))
if str1 == "Deposit":
    own.deposit(int(input("Write the amount: ")))
