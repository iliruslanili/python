with open('lesson5_task6.txt', 'r') as f:
    lines = f.readlines()
    themes = {}
    for line in lines:
        count = sum([int(i[:i.find('(')]) for i in line.split()[1:] if i != '—'])
        themes[line[:line.find(' ')]] = count

print(themes)
