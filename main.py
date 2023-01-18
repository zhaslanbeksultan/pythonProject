#Intro//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Hello, World!")

#Syntax/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if 3 > 2:
  print("Yahoo!!!")

# Python_Variables///////////////////////////////////////////////////////////////////////////////////////////////////////
x, y, z = "O", "a", "e"
print(x)
print(y)
print(z)

x = y = z = "float"
print(x)
print(y)
print(z)

animals = ["dog", "cat"]
a, b = animals
print(a, "-", b)

x = "Python "
y = "is "
z = "awesome"
print(x + y, z)

x = "awesome"


def f():
    print("Python is", x)


f()

D = "awesome"


def myfunc():
    D = "fantastic"
    print("Python is " + D)


myfunc()
print("Python is " + D)

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# Data Types//////////////////////////////////////////////////////////////////////////////////////////////////////////////
word = "abcdefghijklmnopqrstuvwxyz"
print(type(word))
wow = 26526j
print(type(wow))
bb = bytes(56)
print(type(bb))
print(bb)

# Numbers////////////////////////////////////////////////////////////////////////////////////////////////////////////////
x = -51313133131313265122222222222222222222222222222222222222222222222222222222222222222222222222222222
print(x)
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 5.5
a = int(x)
print(x, a)
print(type(x), type(a))

import random
print(random.randrange(1, 9))

# Casting////////////////////////////////////////////////////////////////////////////////////////////////////////////////
x = int(1)
y = int(2.8544)
z = float("3.5")
print(x, y, z)

# Strings////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """lllllllllllllllllllllllllll
llllllllllllllllllllllllllllllll
llllllllllllllllllllllllllllllll"""
print(a)

a = "Hello, World!"
print(a[12])

for i in "word":
    print(i)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are ree!"
if "free" in txt:
  print("Yes, 'free' is present.")
else:
    print("NO")

text = "Hell, World!"
if "Hello" in text:
    print("Awesome!")
if "Hello" not in text:
    print("Oh no!")

b = "Hello, World!"
print(b[2:3])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "H"
print(a.replace("H","J"))

a = "Hello, World!"
print(a.split(","))

a="und"
b="prkmf0"
c=a+b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

n=95
m=45
c="nrnvdok ieqmfc {1} l,wled, {0}"
print(c.format(n, m))

n=95
m=45
c="nrnvdok ieqmfc {0} l,wled, {1}"
print(c.format(n, m))

text="oiwnevo \niefiemi\" jwdjo"
print(text)

#Booleans///////////////////////////////////////////////////////////////////////////////////////////////////////////////
print (10>9)
print(10>5)
