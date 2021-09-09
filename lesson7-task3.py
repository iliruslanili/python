class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, cells_per_row):
        out = ''
        used = 0
        while used != self.cells:
            used += 1
            out += '*' if used % cells_per_row else '*\n'
        return out

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            print('Разность клеток не больше 0!')
            return None

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        if other.cells > 0:
            return round(self.cells / other.cells)
        else:
            print('Некорректный знаменатель!')
            return None

    def __str__(self):
        return f'{self.cells}'


if __name__ == '__main__':
    cell1 = Cell(12)
    cell2 = Cell(20)
    print(cell1.make_order(5))
    print(cell2.make_order(5))
    print(cell1 + cell2)
    print(cell1 - cell2)
    print(cell1 * cell2)
    print(cell1 / cell2)
