class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = ' '.join([self.name, self.surname])
        return full_name


    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

p1 = Position(name='Adam', surname='Sandler', position='Operator', wage=50000, bonus=10000)
print(p1.name)
print(p1.surname)
print(p1.position)
print(p1._income)
print(p1.get_full_name())
print(p1.get_total_income())
