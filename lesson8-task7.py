import math


class Complex:

    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

    def __add__(self, other):
        return Complex(self.real + other.real, self.imagine + other.imagine)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imagine - other.imagine)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imagine ** 2)

    def __mul__(self, other):
        real = (self.real * other.real - self.imagine * other.imagine)
        imagine = (self.real * other.imagine + other.real * self.imagine)
        return Complex(real, imagine)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imagine * other.imagine) / (other.real**2 + other.imagine**2)
        imagine = (other.real * self.imagine - self.real * other.imagine) / (other.real**2 + other.imagine**2)
        return Complex(real, imagine)

    def __str__(self):
        real = self.real
        imagine = self.imagine
        return f'{real if real != 0 else ""}{"+" if imagine > 0 and real != 0 else ""}{imagine}j'


if __name__ == '__main__':
    # Самописное комплексное число
    z1 = Complex(3, 2)
    z2 = Complex(2, -3)
    # Встроенное комплексное число
    z11 = complex(3, 2)
    z22 = complex(2, -3)

    print('Сложение: ')
    print(z1 + z2)      # 5-1j
    print(z11 + z22)    # (5-1j)

    print('Разность: ')
    print(z1 - z2)      # 1+5j
    print(z11 - z22)    # (1+5j)

    print('Умножение: ')
    print(z1 * z2)      # 12-5j
    print(z11 * z22)    # (12-5j)

    print('Деление: ')
    print(z1 / z2)      # 1.0j
    print(z11 / z22)    # (-0+1j)

    print('Модуль: ')
    print(abs(z2))      # 3.605551275463989
    print(abs(z22))     # 3.605551275463989
