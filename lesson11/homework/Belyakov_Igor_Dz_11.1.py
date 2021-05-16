class Date:
    def __init__(self, date):
        self.day, self.month, self.year = self.extract_parts(date)
        self.validate(self.day, self.month, self.year)

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year:04}'

    @classmethod
    def extract_parts(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if not (1 <= month <= 12):
            raise ValueError('Месяц должен быть в пределах 1-12')
        if month == 2:
            last_day = 29 if year % 4 == 0 and year % 100 != 0 or year % 1000 == 0 else 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            last_day = 31
        else:
            last_day = 30

        if not (1 <= day <= last_day):
            raise ValueError(f'День должен быть в пределах 1-{last_day}')


dates = [
    '10-11-2000',
    '10-13-2000',
    '31-11-2000',
    '29-2-2000',
    '29-2-2001',
    '30-2-2000',
    '33-1-2000',
]

for date in dates:
    try:
        dt = Date(date)
        print(dt)
    except ValueError as e:
        print('Неверный формат:', e)
