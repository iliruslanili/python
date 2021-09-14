class Storage:

    def __init__(self):
        pass

    def take(self):
        pass

    def give(self):
        pass


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
