from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.colors_and_times = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        try:
            for color, time in cycle(self.colors_and_times.items()):
                self.__color = color
                print(f'currend color: {self.__color}')
                sleep(time)
        except KeyboardInterrupt:
            print('Work stopped')


obj = TrafficLight()
obj.running()
