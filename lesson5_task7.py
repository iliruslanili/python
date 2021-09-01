from pprint import pprint

stats = [{}, {'average_profit': 0}]
with open('lesson5_task7.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        firm = line.split()
        profit = int(firm[2]) - int(firm[3])
        stats[0][firm[0]] = profit
        if profit >= 0:
            count += 1
            stats[1]['average_profit'] += profit
    stats[1]['average_profit'] /= count

pprint(stats)
