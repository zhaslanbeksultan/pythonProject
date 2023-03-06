import os
path = 'C:\\Users\\zhasl\\PycharmProjects\\pythonProject'
#Program to list only directories.
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)

#Program to list only files and all directories.
print(os.listdir(path))

#Program to list only files.
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)

# Test the existence, readability, writability and executability of the specified path.
path = 'C:\\Users\\zhasl\\PycharmProjects\\pythonProject\\Lab6\\dir_and_files\\1.py'
print("Exist:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

# Write a Python program to test whether a given path exists or not.
print("A path exists:", os.path.exists(path))

# If the path exist find the filename and directory portion of the given path.
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))

# Write a Python program to count the number of lines in a text file.
with open(r"text.txt", 'r') as text:
    # print(text.readlines())
    lines = len(text.readlines())
    print('Total Number of lines:', lines)

# Write a Python program to write a list to a file.
list1 = ["Acer", "Asus", "Lenovo"]
with open(r'text2.txt', 'w') as text2:
    text2.write("list1:\n ")
    for i in list1:
         text2.write("-->"+i + "\n ")
    text2.close()
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# change directory
import string
os.mkdir('A-Z')
for i in string.ascii_uppercase:
    with open(f"A-Z\\{i}.txt", 'w') as j:
        j.write(f"This is {i}.txt file")
    j.close()
# Write a Python program to copy the contents of a file to another file
with open("text.txt") as f:
    with open("text3.txt", "w") as f1:
        for line in f:
            f1.write(line)
    f1.close()

# Write a Python program to delete file by specified path.
with open('delete.txt', 'w') as d:
    d.write("NOIndrkfvnksdmvjdwi")
d.close()
print(os.getcwd())
if os.path.exists('C:\\Users\\zhasl\\PycharmProjects\\pythonProject\\Lab6\\dir_and_files\\delete.txt'):
    os.remove('delete.txt')