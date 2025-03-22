list = ["apple", "pear", "banana", "grapes", "pineapple"]

file = open("2025-03-22/fruit.txt","w")

for item in list:
    file.write(item)
    file.write("\n")

file.close()