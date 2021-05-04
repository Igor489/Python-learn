import random


class Car:
    speed_limit = None

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0
        self.direction = 'Север'

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

    def is_police(self):
        return False

    def get_status(self):
        police_text = 'POLICE ' if self.is_police() else ''

        overspeed_text = ' ПРЕВЫШЕНИЕ!' if self.speed_limit and self.speed > self.speed_limit else ''
        if self.speed > 0:
            return f'{police_text}{self.color} {self.name} двигается со скоростью {self.speed}{overspeed_text} на {self.direction}'
        else:
            return f'{police_text}{self.color} {self.name} стоит'


class TownCar(Car):
    speed_limit = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40


class PoliceCar(Car):
    def is_police(self):
        return True


cars = [
    TownCar('серый', 'Бьюик'),
    SportCar('красный', 'Ламборгини'),
    WorkCar('желтый', 'Камаз'),
    PoliceCar('белый', 'Мерседес'),
]

for iteration in range(5):
    for car in cars:
        action = random.randint(1, 3)
        if action == 1:
            car.go(random.randint(10, 100))
        elif action == 2:
            car.turn(random.choice(['Север', 'Юг', 'Запад', 'Восток']))
        elif action == 3:
            car.stop()
        print(car.get_status())
