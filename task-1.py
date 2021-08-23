# С помощью if else
def div(arg1: float, arg2: float):
    return arg1 / arg2 if arg2 != 0 else 'Деление на ноль!'


# С помощью исключения
# Предыдущая функция переопределяется. Работает она точно также, как и эта. По скорости работы не проверял
def div(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return 'Деление на ноль!'


print(div(1, 1))  # 1.0
print(div(1, 0))  # Деление на ноль!
print(div(0, 1))  # 0.0
print(div(100, 2.3))  # 43.47826086956522
print(div(100, 2.3 - 2.3))  # Деление на ноль!
print(div(100, 0.0000000000000000001))  # 1e+21
