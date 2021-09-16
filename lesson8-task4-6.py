from abc import ABC, abstractmethod


class StorageOverflow(Exception):
    def __init__(self, message):
        self.message = message


class EquipmentNotFound(Exception):
    def __init__(self, message):
        self.message = message


class EmptyStorage(Exception):
    def __init__(self, message):
        self.message = message


class Department(ABC):

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

    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.container = []

    def take(self, obj):
        if self.is_full:
            raise StorageOverflow('Storage is full')
        else:
            self.container.append(obj)

    def give(self, name):
        index = self.find(name)
        if self.is_empty:
            raise EmptyStorage('Storage is empty')
        elif index is not None:
            return self.container.pop(index)
        else:
            raise EquipmentNotFound(f'{name} not found in storage')

    @property
    def is_full(self):
        return False if len(self.container) < self.max_size else True

    @property
    def is_empty(self):
        return False if len(self.container) > 0 else True

    def find(self, name):
        for i, obj in enumerate(self.container):
            if obj.name == name:
                return i
        return None


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
    obj1 = Printer('Brother DCP-1512R', (40, 40, 50), 5, 200)
    print(obj1.name)
