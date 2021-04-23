def merge_tutors_and_classes(tutors, klasses):
    for i, tutor in enumerate(tutors):
        klass = klasses[i] if i < len(klasses) else None
        yield tutor, klass


tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

g = merge_tutors_and_classes(tutors, klasses)
print(type(g))

for value in g:
    print(value)
