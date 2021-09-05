class Road:
    def __init__(self, length, width, mass, thickness):
        self.length = length
        self.width = width
        self.mass = mass
        self.thickness = thickness


    def calc(self):
        mass = self.length * self.width * self.mass * self.thickness
        return mass


obj = Road(20, 5000, 25, 5)
print(obj.calc())
