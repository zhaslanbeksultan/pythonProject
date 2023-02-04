#Functions//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1////////////////////////////////
def c_ounces (grams):
    print(28.3495231 * grams)
grams = float(input())
c_ounces(grams)

#2/////////////////////////////////
def c_centigrade (F):
    print((5 / 9) * (F-32))


F = float(input())
c_centigrade(F)

#3/////////////////////////////////
def solve(numheads, numlegs):
    r = ((numlegs - (numheads * 2))*2)/4
    ch = numheads - r
    str1 = "Number of rabbits: " + str(r) + "\nNumber of chickens: " + str(ch)
    return str1

numheads = 35
numlegs = 94
print(solve(numheads, numlegs))

#4/////////////////////////////////

def filter_prime(nums, list2):
    for i in nums:
        a = 0
        for j in range(2, i):
            if i // j == i / j:
                a += 1
        if a < 1:
            list2.append(i)

    if nums.index(i) == len(nums)-1:
        return list2
nums = list(map(int,input().split()))
list2 = []
print(filter_prime(nums, list2))

#5/////////////////////////
import itertools
abc = list(map(str, input("Write a string: ")))
permutations = list(itertools.permutations(abc))
print([''.join(permutation) for permutation in permutations])

#6/////////////////////////////////////////////////////////////////////////////////
def p(str1):
    list1 = list(map(str,str1.split()))
    list1.reverse()
    str2 = ""
    for i in list1:
        str2 += i + " "
    return str2

str1 = input()
print(p(str1))

#7////////////////////////////////////////////////
def has_33(nums):
    for i in range(1,len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    else:
        return False
nums = list(map(int,input().split()))
print(has_33(nums))


# 8//////////////////////////////////////////////////
def spy_game(nums):
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    for k in range(j + 1, len(nums)):
                        if nums[k] == 7:
                            return True
    else:
        return False


nums = list(map(int, input().split(',')))
print(spy_game(nums))

#9/////////////////////////////////////////////////////////
import math
def volume(r):
    return (4/3) * (math.pi) * (r**3)
r = float(input())
print(volume(r))


# 10////////////////////////////////////////
def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)


list1 = list(map(str, input().split()))
unique(list1)


# 11///////////////////////////////
def Palindrome(str1):
    return str1 == str1[::-1]


str1 = input()
ans = Palindrome(str1)

if ans:
    print("Yes, palindrome")
else:
    print("Not polindrome")

#12/////////////////////////////////////////////
def histogram(list1):
    for i in list1:
        print("*" * i)

list1 = list(map(int, input().split(', ')))
histogram(list1)

#13//////////////////////////////////////////////////////////
def f_guess(num, guess):
    if guess < num:
        print('Your guess is too low.')
        return False
    if guess > num:
        print('Your guess is too high.')
        return False
    if guess == num:
        return True

import random
t = 0
print('Hello! What is your name?')
name = input()
num = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
while True:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    t += 1
    b = f_guess(num, guess)
    if b == True:
        print('Good job, ' + name + '! You guessed my number in ' + str(t) + ' guesses!')
        break
