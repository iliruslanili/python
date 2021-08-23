import math


def custom_pow(arg1: int, arg2: int) -> float:
    return arg1 ** arg2


def custom_pow(arg1: int, arg2: int) -> float:
    x = 1
    for _ in range(abs(arg2)):
        x *= arg1
    return float(x) if arg2 >= 0 else 1 / x


def custom_pow_log(arg1: int, arg2: int) -> float:
    p = math.exp(arg2 * math.log(arg1))
    return p


x, y = 2, -2
print(x ** y)  # 0.25
print(custom_pow(x, y))  #0.25
print(custom_pow_log(x, y))  # 0.25
