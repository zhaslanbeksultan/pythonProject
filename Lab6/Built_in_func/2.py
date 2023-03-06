# Write a Python program with builtin function to multiply all the numbers in a list
import math
list1 = [5,6,6,2,6,2,6,2,6]
print(math.prod(list1))

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
str1 = input("Enter a string: ")
u,l = 0,0
for i in str1:
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print(f"The number of upper case letters: {u}\nThe number of lower case letters: {l}")

# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
str2 = input("Enter a string to check for palindrome: ")
print(str2 == ''.join(reversed(str2)))

# Write a Python program that invoke square root function after specific milliseconds.
# Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
import math as m, time as t
def delay_sqrt(ms, n):
    t.sleep(ms/1000)
    return m.sqrt(n)
print(delay_sqrt(int(input("Enter a ms: ")), int(input("Enter a number you want to sqrt: "))))

# Write a Python program with builtin function that returns True if all elements of the tuple are true.
tuple1 = (True, "Python", 0)
print(all(tuple1))