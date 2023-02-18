#1/////////////////////////////////
import math
def converter(x):
    return math.radians(x)

x = int(input("Enter a number: "))
print(converter(x))

#2/////////////////////////////////
import math
def t_area(h, u, l):
    return ((u + l) / 2 ) * h

h = int(input("Height: "))
u = int(input("Upper bound: "))
l = int(input("Lower bound: "))
print("Area of Trapezoid is = " + str(t_area(h, u, l)))

#3/////////////////////////////////
import math
def p_area(n, l):
    return math.floor((n * l * (l /( 2 * math.tan(math.radians(180 / n)))))/2)

n = int(input("Number of sides: "))
l = int(input("Length of one side: "))
print("Area of Polygon is = " + str(p_area(n, l)))

#4/////////////////////////////////
import math
def p_area(h, b):
    return h * b
b = int(input("The length of base: "))
h = int(input("The length of height: "))
print("Area of Parallelogram is = " + str(p_area(h, b)))