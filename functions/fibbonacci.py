def fibonacci(e):
    print("calculating fib ", e)
    if e == 0 :
        return 0 
    elif e == 1 or e == 2:
        return 1
    return fibonacci(e-1) + fibonacci(e-2)

    
num1 = int(input("Enter a number: "))

result = fibonacci(num1)
print(result)