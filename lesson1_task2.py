# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60 if seconds // 60 < 60 else seconds % 60
total_minutes = seconds // 60
hours = total_minutes // 60
print(f'{hours}:{minutes:02}:{seconds%60:02}')
