class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position:
    def __init__(self, worker, position, income):
        self.worker = worker
        self.position = position
        self._income = income

    def get_full_name(self):
        return self.worker.name + ' ' + self.worker.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


emp = Worker('Иван', 'Петров')
position = Position(emp, 'Директор', {'wage': 1000, 'bonus': 200})

print(f'Сотрудник: {position.get_full_name()}, доход: {position.get_total_income()}')
