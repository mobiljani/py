def sum(a, b):
    ans = a + b
    
    return ans

num1 = int(input("Enter a number: "))
print("Enter another number.")
num2 = int(input())

result = sum(num1, num2)

print(f"{num1} plus {num2} is {result}")