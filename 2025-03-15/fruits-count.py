
"""""
Reads the file, and counts the amount of lines in it.

"""

fruits = open("2025-03-15/fruits.txt","r")
total = 0
for line in fruits:
    total = total + 1

print(total)

fruits.close()