from abc import ABC, abstractmethod


class StorageOverflow(Exception):
    """
    Возникает при переполнении хранилища отдела/склада
    """
    def __init__(self, message):
        self.message = message


class EquipmentNotFound(Exception):
    """
    Возникает при отсутствии объекта в хранилище отдела/склада
    """
    def __init__(self, message):
        self.message = message


class EmptyStorage(Exception):
    """
    Возникает при попытке поиска в пустом хранилище отдела/склада
    """
    def __init__(self, message):
        self.message = message


# Композиция?
class Company:
    """
    Класс предприятия. Содержит метод, передающий технику из одного отдела в другой.
    Например, передача принтера со склада в какой либо отдел и обратно
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def exchange(cls, name: str, source: object, destination: object):
        try:
            obj = source.give(name)
            destination.take(obj)
            print(f'{name} transferred from {source.name} to {destination.name}')
        except Exception as e:
            print(e)


class Department(ABC):
    """
    Абстрактный класс отделений предприятия
    """

    @abstractmethod
    def take(self, obj):
        pass

    @abstractmethod
    def give(self, name):
        pass

    @abstractmethod
    def find(self, name):
        pass


class Storage(Department):
    """
    Класс склада, унаследованный от абстрактного класса Департамент. Содержит ограниченное хранилище
    """

    def __init__(self, name, max_size):
        """
        Конструктор класса склада. Принимает имя склада и максимальное количество вмещаемой техники
        :param name: название склада
        :param max_size: максимальное количество вмещаемой техники
        """
        self.name = name
        self.max_size = max_size
        self.container = []  # Сюда будем складывать все объекты (оргтехнику)

    def take(self, obj):
        """
        Метод для принятия объекта (оргтехники) на склад. При переполнении бросается исключение
        :param obj: объект, принимаемый на склад
        :return: None
        """
        if self.is_full:
            raise StorageOverflow('Storage is full')
        else:
            self.container.append(obj)

    def give(self, name: str) -> object:
        """
        Метод выдачи объекта со склада. Проверяется наличие объекта на складе по названию.
        При отсутствии объекта на складе бросается исключение.
        Удаляет объект из хранилища склада и возвращает данный объект
        :param name: Название оргтехники, которую нужно забрать со склада
        :return: Объект
        """
        index = self.find(name)
        if self.is_empty:
            raise EmptyStorage('Storage is empty')
        elif index is not None:
            return self.container.pop(index)
        else:
            raise EquipmentNotFound(f'{name} not found in storage')

    @property
    def is_full(self) -> bool:
        """
        Метод проверки достижения максимально допустимого количества техники на складе
        :return: True если склад полон, иначе False
        """
        return False if len(self.container) < self.max_size else True

    @property
    def is_empty(self) -> bool:
        """
        Метод проверки на пустоту склада
        :return: False если склад не пуст, иначе True
        """
        return False if len(self.container) > 0 else True

    def find(self, name: str):
        """
        Метод поиска техники на складе по названию
        :param name: название оргтехники
        :return: индекс первого попавшегося объекта по названию или None, если такого объекта нет
        """
        for i, obj in enumerate(self.container):
            if obj.name == name:
                return i
        return None

    def stats(self) -> dict:
        names = [i.name for i in self.container]
        stat = {k: names.count(k) for k in set(names)}
        return stat

    def __str__(self):
        return f'{dict({self.name: self.stats()})}'


class OfficeEquipment:

    def __init__(self, name: str, size: tuple, weight: int):
        self.name = name
        self.size = size
        self.weight = weight


class Printer(OfficeEquipment):

    def __init__(self, name: str, size: tuple, weight: int, paper_capacity: int, print_speed: int, color_print: bool):
        super().__init__(name, size, weight)
        self.paper_capacity = paper_capacity
        self.print_speed = print_speed


class Scanner(OfficeEquipment):

    def __init__(self, name: str, size: tuple, weight: int, scan_speed: int, paper_size: str):
        super().__init__(name, size, weight)
        self.paper_size = paper_size
        self.scan_speed = scan_speed


class Phone(OfficeEquipment):

    def __init__(self, name: str, size: tuple, weight: int, memory: int, wireless: bool):
        super().__init__(name, size, weight)
        self.memory = memory
        self.wireless = wireless


if __name__ == '__main__':

    # Генерируем экземпляры классов оргтехники
    printers = [Printer('Brother DCP-1512R', (40, 40, 50), 5, 200, 18, True) for _ in range(3)]
    phones = [Phone('Phillips A100', (10, 10, 20), 1, 200, True) for _ in range(2)]
    scanners = [Scanner('Xerox Phaser WF72', (50, 50, 20), 4, 3, 'A4') for _ in range(5)]

    storage = Storage('Склад 1', max_size=20)

    # Не стал создавать отдельный класс для отделов, поэтому решил просто создать экземпляр отдела из класса склада.
    # Этого достаточно для реализации обмена техникой между отделами
    it_department = Storage('Департамент информационных технологий', max_size=5)

    for printer in printers:
        try:
            storage.take(printer)
        except StorageOverflow:
            print('Склад полон!')

    for phone in phones:
        try:
            storage.take(phone)
        except StorageOverflow:
            print('Склад полон!')

    for scanner in scanners:
        try:
            storage.take(scanner)
        except StorageOverflow:
            print('Склад полон!')

    # Вывод содержимого склада и отдела перед передачей
    print(f'Before:\n{storage}')
    print(it_department)

    # Передадим со склада в отдел принтер
    Company.exchange('Brother DCP-1512R', storage, it_department)
    Company.exchange('Brother DCP-1512R', storage, it_department)
    Company.exchange('Brother DCP-1512R', storage, it_department)
    Company.exchange('Phillips A100', storage, it_department)

    # Вывод содержимого склада и отдела перед передачей
    print(f'After:\n{storage}')
    print(it_department)
