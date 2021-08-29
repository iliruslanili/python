import sys

hours = int(sys.argv[1])
hour_price = int(sys.argv[2])
prize = int(sys.argv[3])
pay = hours * hour_price + prize

print(f'Заработная плата: {pay}')
