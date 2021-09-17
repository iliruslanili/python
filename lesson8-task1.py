import regex as re


class InvalidDateFormat(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    day, month, year = 1, 1, 1970

    def __init__(self, inp: str):
        self.inp = inp
        is_valid = True if re.findall('\d\d-\d\d-\d{4}', inp) else False
        if not is_valid:
            raise InvalidDateFormat('Неверный формат даты!')

    @classmethod
    def extract(cls, string) -> None:
        """
        Разделяет входную строку на день, месяц и год
        :param string:
        :return: tuple
        """
        try:
            cls.day, cls.month, cls.year = tuple(map(int, string.split('-')))
        except:
            raise InvalidDateFormat('Неверный формат даты!')
        pass

    @staticmethod
    def validate(inp) -> bool:
        """
        Проверка даты на правильность. Проверяется допустимый диапазон дня, месяца и года.
        Дополнительная проверка диапазона дней для февраля.
        :param inp:
        :return: bool
        """
        is_valid = True if inp.year > 0 else False
        leap = Date.is_leap_year(inp.year)
        if inp.month not in range(1, 13) and inp.day not in range(1, 31):
            is_valid = False
        if leap and inp.month == 2 and inp.day not in range(1, 30):
            is_valid = False
        if not leap and inp.month == 2 and inp.day not in range(1, 29):
            is_valid = False
        if not is_valid:
            raise InvalidDateFormat('Такой даты не существует!')
        return is_valid

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Проверка, високосный ли год. Возвращает True, если год високосный и False если невисокосный
        :param year:
        :return: bool
        """
        return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year}'


sample1 = Date('01-02-2021')
sample1.extract(sample1.inp)
print(f'Дата: {sample1}')
print(f'Дата правильная: {sample1.validate(sample1)}')
print(f'Високосный год: {sample1.is_leap_year(sample1.year)}')


# Исключение InvalidDateFormat "Такой даты не существует!"
# sample2 = Date('31-02-2021')
# sample2.extract(sample2.inp)
# print(f'Дата: {sample2}')
# print(f'Дата правильная: {sample2.validate(sample1)}')
# print(f'Високосный год: {sample2.is_leap_year(sample2.year)}')


# Ислючение InvalidDateFormat "Неверный формат даты!"
# sample3 = Date('lol kek cheburek')
# sample3.extract(sample3.inp)
# print(f'Дата: {sample3}')
# print(f'Дата правильная: {sample3.validate(sample3)}')
# print(f'Високосный год: {sample3.is_leap_year(sample3.year)}')
