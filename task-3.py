# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

try:  # Защита от ввода не числа
    val = int(input('Введите число: '))
    print(val + val * 11 + val * 111)
except:
    print('Введите корректное число')