with open('lesson5_task2.txt', 'r') as f:
    lines = f.readlines()
    print()
    lines_count = len(lines)
    words_count = sum(map(lambda x: len(x.split(' ')), lines))

print(f'Lines: {lines_count}')
print(f'Words: {words_count}')
