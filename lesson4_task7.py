def factorial(n):
    mul = 1
    for i in range(1, n):
        mul *= i
        yield mul


for num, val in enumerate(factorial(5), 1):
    print(f'{num}! = {val}')
