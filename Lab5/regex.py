import re
#1////////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
pattern = r'ab*'

for x in f:
    match = re.findall(pattern, x)
    if match:
        print(x)
#2////////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
pattern = r'ab{2,3}'

for x in f:
    match = re.findall(pattern, x)
    if match:
        print(x)
#3////////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
pattern = r'[a-z]+_[a-z]+'

for x in f:
    match = re.findall(pattern, x)
    if match:
        print(x)
#4///////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
pattern = r'[A-Z]{1}[a-z]+'

for x in f:
    match = re.findall(pattern, x)
    if match:
        print(match)
#5//////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
pattern = r'a.*b$'

for x in f:
    match = re.findall(pattern, x)
    if match:
        print(match)
#6///////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
text = f.read()
result = re.sub("[ ,.]", ":", text)
print(result)

#7///////////////////////////////////////
word = input("Enter you snake_case word: ")
list1 = re.split("_", word)

for i in range(1, len(list1)):
    list1[i] = list1[i].capitalize()
print(''.join(list1))

#8///////////////////////////////////////
f = open("row.txt", "r", encoding='utf-8')
text = f.read()
list1 = re.split(".[A-Z]", text)
for i in list1:
    print(i)

#9///////////////////////////////////////
text = input("Enter a string: ")
str1 = re.sub('([a-z])([A-Z])', r'\1 \2', text)
print(str1)

#10///////////////////////////////////////
text = input("Enter a string: ")
str1 = re.sub('([a-z])([A-Z])', r'\1_\2', text)
print(str1.lower())