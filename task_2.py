from random import randint

source = [randint(-100, 100) for _ in range(10)]
result = [source[i] for i in range(1, len(source)) if source[i] > source[i - 1]]
print(source)
print(result)
