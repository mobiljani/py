numbers = open("2025-03-15/numbers.txt","r")
numlist = []
total = 0
for line in numbers:
    l = int(line.strip())
    numlist.append(l)
    total = total + l 

print(numlist)
print(total)

numbers.close()