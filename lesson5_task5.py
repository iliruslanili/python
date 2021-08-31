from random import randint

with open('lesson5_task5.txt', 'w') as f:
    f.write(' '.join([str(randint(-10, 10)) for _ in range(20)]))

with open('lesson5_task5.txt', 'r') as f:
    print(sum(map(int, f.readlines()[0].split())))
