people = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]
for human in people:
    words = human.split()
    name = words[-1].title()
    print(f'Привет, {name}!')
