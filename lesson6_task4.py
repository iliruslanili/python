class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Current speed: {self.speed}')
        return self.speed

    def go(self):
        self.speed = self.speed if self.speed != 0 else 40
        if self.is_police:
            print(f'Woop Woop! {self.name} is going')
        else:
            print(f'{self.name} is going')

    def stop(self):
        print('Car stopped')
        self.speed = 0

    def turn(self, direction):
        print(f'Turning to the {direction}')


class TownCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > 60:
            print('Speed violation!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > 40:
            print('Speed violation!')


police = Car(speed=100, color='blue', name='LSPD', is_police=True)
print(police.name)
print(police.speed)
print(police.color)
print(police.is_police)
police.go()
police.stop()
police.turn('right')

town = TownCar(speed=90, color='red', name='Tuareg')
print(town.name)
print(town.speed)
print(town.color)
print(town.is_police)
town.go()
town.stop()
town.turn('left')

work = WorkCar(speed=40, color='white', name='Yandex.Delivery')
print(work.name)
print(work.speed)
print(work.color)
print(work.is_police)
work.go()
work.stop()
work.turn('30 degrees to right')
