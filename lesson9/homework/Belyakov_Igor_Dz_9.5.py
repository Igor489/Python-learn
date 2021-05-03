class Stationery:
    def draw(self):
        print('Запуск отрисовки')

class Pen:
    def draw(self):
        print('Я ручка, я ручка')

class Pencil:
    def draw(self):
        print('Я карандаш, я карандаш')

class Handle:
    def draw(self):
        print('Я маркер, я маркер')


stationery = [Stationery(), Pen(), Pencil(), Handle()]
for Stationery in stationery:
    Stationery.draw()
