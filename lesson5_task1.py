inp = input('Введите строку для записи в файл: ')
with open('lesson5_task1.txt', 'w') as file:
    while inp != '':
        file.writelines(inp + '\n')
        inp = input('Введите строку для записи в файл: ')
