from functools import reduce

source = [i for i in range(100, 1001, 2)]
result = reduce(lambda x, y: x * y, source)
print(result)
