# #Class//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# #1///////////////////////////
class strupp():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input()
    def printString(self):
        print(self.str1.upper())
str1 = strupp()
str1.getString()
str1.printString()
#2//////////////////////////
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length**2

a = Square(int(input("Введите длину края фигуры: ")))
print(a.area())
print(Square().area())

#3///////////////////////////////////
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

Area = Rectangle(int(input("Введите длину прямоугольника: ")),int(input("Введите ширину прямоугольника: ")))
print("Площадь прямоугольника: " + str(Area.area()))

#4/////////////////////////
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return f"The coordinates of the point are ({self.x}, {self.y})"
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        return f"The coordinates of the point are ({self.x}, {self.y})"
    def dist(self, x2, y2):
        xd = abs(self.x - x2)
        yd = abs(self.y - y2)
        return "Distance between two points is " + str(math.sqrt(xd**2 + yd**2))
point = Point(int(input("X-axis coordinate: ")), int(input("Y-axis coordinate: ")))
print(point.show())
print(point.move(int(input("Changes on the X-axis: ")), int(input("Changes on the X-axis: "))))
print(point.dist(int(input("Coordinates of the next point on the X-axis: ")), int(input("Coordinates of the next point on the Y-axis: "))))

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

#6/////////////////////////////
class num():
    def __init__(self, list1):
        self.list1 = list1
    def is_prime(self):
        p_list = []
        for i in self.list1:
            x = 0
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    x += 1
            if x == 0:
                p_list.append(i)
        return p_list

list1 = list(map(int, input("Write a list of numbers: ").split()))
obj = num(list1)
print(obj.is_prime())
#6_lambda/////////////////////////////////
class filt():
    def __init__(self, list1):
        self.list1 = list1
    def is_prime(self):
        return list(filter(lambda i: all(i % j != 0 for j in range(2, i//2)), list1))

list1 = list(map(int, input("Write a list of numbers: ").split()))
obj = filt(list1)
print(obj.is_prime())