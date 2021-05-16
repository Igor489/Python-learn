class Matrix:
    def __init__(self, rows):
        if len(rows) == 0 or len(rows[0]) == 0:
            raise ValueError('Количество колонок и строк в матрице не должно быть нулем')

        length = None
        for row in rows:
            if length is not None and length != len(row):
                raise ValueError('Строки в матрицы должны быть одинаковой длины')
            length = len(row)

        self.rows = rows

    @property
    def size(self):
        return len(self.rows), len(self.rows[0])

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError('Для сложения матрицы должны быть одинакового размера')

        rows = [
            [
                self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[i]))
            ] for i in range(len(self.rows))
        ]
        return Matrix(rows)

    def __str__(self):
        return '\n'.join(
            " ".join(
                f'{value:3}' for value in row
            )
            for row in self.rows
        )


m = Matrix([[1,2,3], [4,5,6]])
print('m', m.size)
print(m)
print('---')

m2 = Matrix([[3,3,3], [2,2,2]])
print('m2', m2.size)
print(m2)
print('---')

m3 = m + m2
print('m3')
print(m3)
print('---')
