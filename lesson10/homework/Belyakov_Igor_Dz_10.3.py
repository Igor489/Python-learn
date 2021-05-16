class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if other.cells > self.cells:
            raise ValueError('Вычитать можно только из большей клетки меньшую')

        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def print(self, columns):
        # print(self.cells)
        for i in range(self.cells // columns):
            print('*' * columns)
        if self.cells % columns > 0:
            print('*' * (self.cells % columns))


c1 = Cell(10)
print('c1')
c1.print(6)
print('---')

c2 = Cell(21)
print('c2')
c2.print(6)
print('---')


# ++++
c3 = c1 + c2
print('c3')
c3.print(6)
print('---')

c1 = Cell(10)
print('c1')
c1.print(6)
print('---')

c2 = Cell(21)
print('c2')
c2.print(6)
print('---')


# ----
try:
    c4 = c1 - c2
except ValueError as e:
    print(e)
else:
    print('c4 ++++')
    c4.print(6)
    print('---')

c5 = c2 - c1
print('c5')
c5.print(6)
print('---')

c6 = c2 * c1
print('c6')
c6.print(6)
print('---')

c6 = c2 * c1
print('c6')
c6.print(30)
print('---')

c6 = c2 * c1
print('c6')
c6.print(15)
print('---')

c7 = c2 / c1
print('c7')
c7.print(6)
print('---')
