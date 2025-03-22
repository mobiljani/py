file = open("2025-03-22/fruit.txt", "r")
file2 = open("2025-03-22/copyfruit.txt", "w")

for item in file:
    file2.write(item)

file.close()
file2.close()