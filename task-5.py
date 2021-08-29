def func(string: str) -> tuple:
    summ = 0
    stop = False
    if string.find('stop') != -1:
        string = string[:string.find('stop')]
        stop = True
    summ += sum([int(i) for i in string.split()])
    return stop, summ


stop = False
summ = 0

while not stop:
    values = input('Введите числа через пробел. Стоп-слово: stop: ')
    stop, s = func(values)
    summ += s
    print(f'Сумма: {summ}')
