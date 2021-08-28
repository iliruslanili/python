from itertools import count, cycle

print('Первый цикл:')
for i in count(3):
    print(i)
    if i == 10:
        break

iterable = ['lol', 'kek', 'cheburek']
print('Второй цикл:')
for i, val in zip(range(20), cycle(iterable)):
    print(val)
