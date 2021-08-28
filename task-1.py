# 1 Задание: Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

# Создаем переменные

integer = 0
string = 'one'
tup = (1, 'two', 3.0, 2+2, [5])
lst = [1, 2, 3]
none = None
boolean = True
scientific_float = 10e-10
simple_float = 0.00000000001

# А вот так переменные именовать нельзя

# 1a = 3 # SyntaxError: invalid syntax
# !b = 4 # SyntaxError: invalid syntax

# но вот так можно)
_e = integer
_ = 9
_4 = 111
_1_2_3 = _4

# Выводим переменные

print(f'Выводим все переменные, определенные выше:'
      f'\nЦелое число: {integer}'
      f'\nСтрока: {string}'
      f'\nКортеж: {tup}'
      f'\nСписок: {lst}'
      f'\nNone: {none}'
      f'\nЛогика: {bool}'
      f'\nScientific notation: {scientific_float}'
      f'\nПлавающая точка: {simple_float}'
      f'\n_e: {_e}'
      f'\n_: {_}'
      f'\n_4: {_4}'
      f'\n_1_2_3: {_1_2_3}')

# Запрашиваем у пользователя что-нибудь

user_input = input('Введите что либо: ')
print(f'Вы ввели: {user_input}')
