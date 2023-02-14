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

#Tuples/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
mytuple=("apple","banana","banana","mango")
print(mytuple)
print(len(mytuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

newtuple = tuple(("smth"))
print(type(newtuple))
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

tup=("tractor","car","bike")
if "bike" in tup:
    print("Yes, \"bike\" is in this tuple")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#Set////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
for x in thisset:
    print(x)
print("banana" in thisset)
thisset.add("watermelon")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
thisset.pop()
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Dictionaries///////////////////////////////////////////////////////////////////////////////////////////////////////////
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1965
}
print(thisdict["year"])
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict["colors"]
x = thisdict.keys()
print(x)
print(thisdict)
print(type(thisdict))
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
x = thisdict.items()
print(x)

x = car.keys()
print(x)
car["color"] = "white"
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#While_Loops////////////////////////////////////////////////////////////////////////////////////////////////////////////
i = 1
while i < 6:
  print(i)
  i += 1

i = 1

while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#For_Loops//////////////////////////////////////////////////////////////////////////////////////////////////////////////
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "apple":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
for x in [0, 1, 2]:
  pass

#Arrays/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars[0])
x = len(cars)
print(x)
for x in cars:
  print(x)

cars.append("Honda")
for x in cars:
  print(x)
cars.pop(1)
cars.remove("Honda")
for x in cars:
  print(x)
