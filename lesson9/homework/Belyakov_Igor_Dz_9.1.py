from datetime import datetime
from time import sleep


class TrafficLight:
    __color = None
    __order = [
        (7, 'red'),
        (2, 'yellow'),
        (6, 'green'),
    ]

    def __init__(self):
        self.__color = 'red'
        self.start_time = datetime.now()
        self.cycle_total_seconds = sum(x[0] for x in self.__order)

    def running(self):
        diff = (datetime.now() - self.start_time).total_seconds()
        shift = diff % self.cycle_total_seconds
        index = 0
        while shift > self.__order[index][0]:
            shift -= self.__order[index][0]
            index += 1

        self.__color = self.__order[index][1]
        return self.__color

light = TrafficLight()
for i in range(15):
    current_time = datetime.now()
    print(current_time, light.running())
    sleep(1.0)
