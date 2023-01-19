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

if(10>5):
    print("Ten is bigger than five")

print(bool("Hello"))
print(bool(0))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Operators//////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(10 / 4)
print(10 // 4)
print(not(10>5 and 10<51))
a, b= 4, 5
print(a is b)

#Lists//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
list = ["apple", "banana", "cherry"]
print(list)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
print(thislist[-2:-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

mylist=['a','b','c','d','e']
if 'a' in mylist:
    print("Yes, \"a\" is in this list")
mylist[2:4]="sdf","adv"
print(mylist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

a=['c','cd']
a.append("cdd")
a.insert(1,'bbb')
a.remove("cd")
a.pop(2)
print(a)
a.clear()
print(a)
del a

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1

[print(x) for x in thislist]

animals =["mouse","dick","dog"]
danimals=[]
for x in animals:
    if "d" in x:
        danimals.append(x)
print(danimals)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
nextlist=[i for i in fruits if i!="cherry"]
print(nextlist)
newlist1 = [x for x in range(10) if x < 5]
print(newlist1)
newlist2=[i.upper() for i in nextlist]
print(newlist2)
newlist3=["halo" for i in nextlist]
print(newlist3)
newlist4=[x if x!=0 else "zero" for x in newlist1]
print(newlist4)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

def myfunc(n):
  return abs(n - 50)
def myfunc1(n):
    return abs(n-82)
thislist = [100, 50, 65, 82, 23]
thislist1=[100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
thislist1.sort(key = myfunc1)
print(thislist)
print(thislist1)

thislist = ["banana", "Orange", "Kiwi","Kawa","karavan","kawa", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list2 = list1 + list2
print(list2)