with open('lesson5_task3.txt') as f:
    lines = f.readlines()
    empl_less_20 = [i.split()[0] for i in lines if int(i.split()[1]) < 20000]
    avg = sum([int(i.split()[1]) for i in lines]) / len(lines)

print('\n'.join(empl_less_20) if empl_less_20 else 'У всех выше 20 000')
print(f'Средняя заработная плата: {avg}')
