# Первая функция делает первую букву прописной в первом слове
# Вторая функция делает первую букву прописной в каждом слове

# P.S. обожаю Python за однострочные решения)
def int_func(string: str):
    return string.capitalize()


def int_func_extended(string: str):
    return ' '.join(i.capitalize() for i in string.split())


print(int_func('some text'))
print(int_func_extended('some text '))
