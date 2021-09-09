from abc import ABC, abstractmethod

class Cloth(ABC):

    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod
    def resources(self):
        pass

class Coat(Cloth):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @property
    def resources(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Cloth):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def resources(self):
        return round(2 * self.height + 0.3, 2)

if __name__ == '__main__':
    myCoat = Coat('Gucci', 38)
    mySuit = Suit('Armani', 180)

    print(f'Coat: {myCoat.name} | resources: {myCoat.resources}')
    print(f'Suit: {mySuit.name} | resources: {mySuit.resources}')
