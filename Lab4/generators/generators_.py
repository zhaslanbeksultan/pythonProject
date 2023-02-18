#1////////////////////////////////
def square_generator(N):
    i = 0
    while i < N:
        i=i+1
        yield i**2

N = int(input("Enter a number: "))
for x in square_generator(N):
    print(x)
#2////////////////////////////////
def even_generator(N):
    i = 0
    while i < N:
        i=i+1
        if i % 2 == 0:
            yield i

N = int(input("Enter a number: "))
list1 = []
for x in even_generator(N):
    list1.append(x)
print(list1)

#3////////////////////////////////
def num_generator(N):
    i = 0
    while i < N:
        i=i+1
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input("Enter a number: "))
for x in num_generator(N):
    print(x)

#4////////////////////////////////
def square(N, M):
    i = N - 1
    while i < M:
        i=i+1
        yield i**2

N = int(input("Enter a first number: "))
M = int(input("Enter a second number: "))
for x in square(N, M):
    print(x)

#5//////////////////////////////////
def n_generator(N):
    i = N + 1
    while i > 0:
        i = i-1
        yield i

N = int(input("Enter a number: "))
for x in n_generator(N):
    print(x)

