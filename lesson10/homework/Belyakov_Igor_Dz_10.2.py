from abc import ABC, abstractmethod
from random import randint


class Clothes(ABC):
    @property
    def cloth_size(self):
        return self.get_size()

    @abstractmethod
    def get_size(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def get_size(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    def get_size(self):
        return 2 * self.height + 0.3


clothes = []
for i in range(10):
    if randint(1, 100) % 2 == 0:
        clothes.append(Coat(randint(5, 9)))
    else:
        clothes.append(Suit(randint(10, 15)))

total_size = 0
for cloth in clothes:
    print(cloth.__class__.__name__, cloth.cloth_size)
    total_size += cloth.cloth_size

print('Всего надо ткани:', total_size)
