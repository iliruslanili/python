def max_sum(arg1: float, arg2: float, arg3: float) -> float:
    return float(max([arg1 + arg2, arg1 + arg3, arg3 + arg2]))


print(max_sum(1, 2, 3))
