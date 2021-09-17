class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

def divide(x, y):
    try:
        if not y:
            raise MyZeroDivisionError('Деление на 0!')
        else:
            return x / y
    except MyZeroDivisionError:
        return 'Попытка деления на 0!'


print(divide(1, 10))
print(divide(10, 0))
