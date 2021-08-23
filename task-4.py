def custom_pow(arg1: int, arg2: int) -> float:
    return arg1 ** arg2


def custom_pow(arg1: int, arg2: int) -> float:
    x = 1
    for _ in range(abs(arg2)):
        x *= arg1
    return float(x) if arg2 >= 0 else 1 / x


x, y = 2, 0
print(x ** y)
print(custom_pow(x, y))
