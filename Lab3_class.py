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