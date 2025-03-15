# write a function which counts the sum or an array

def arraysum(a):
    sum = 0
    for x in a:
        sum = sum + x
    return sum

list = [1, 41, 0, 88, 4, 13, 19, 9, 10, 21]
result = arraysum(list)

print("The sum of the list is: ", result)