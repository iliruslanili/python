# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Способ № 1
maximum, i, string = 0, 0, input('Введите число: ')
while i < len(string):
    maximum = int(string[i]) if int(string[i]) > maximum else maximum
    i += 1
print(maximum)

# Способ № 2
# print(max([int(i) for i in input('Введите число: ')]))
