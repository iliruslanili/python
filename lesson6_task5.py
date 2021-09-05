class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'Pen "{self.title}" is drawing...')

class Pencil(Stationery):
    def draw(self):
        print(f'Pencil "{self.title}" is drawing...')

class Handle(Stationery):
    def draw(self):
        print(f'Handle "{self.title}" is drawing...')
pen = Pen('A')
pencil = Pencil('B')
handle = Handle('C')

pen.draw()
pencil.draw()
handle.draw()
