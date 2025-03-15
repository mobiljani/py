"""
Taking 2 files and displaying each line alternating between the 2"
-Put both txts into their own list
-Printing from 1 file
-Run the for loop based on the amount of lines in a list
"""


fruits = open("2025-03-15/fruits.txt","r")
numbers = open("2025-03-15/numbers.txt","r")

numlist = []
fruitlist = []

for line in fruits:
    fruitlist.append(line.strip())

for line in numbers:
    numlist.append(line.strip())

length = len(numlist)
result = []

for index in range(length):
    print(numlist[index])
    print(fruitlist[index])

fruits.close()
numbers.close()