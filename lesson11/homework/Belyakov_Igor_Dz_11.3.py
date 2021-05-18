class OnlyNumberError(Exception):
    def __init__(self, word):
        self.word = word


def get_number():
    x = input('Введите число:')
    try:
        return int(x)
    except ValueError:
        raise OnlyNumberError(x)


result = []
while True:
    try:
        result.append(get_number())
    except OnlyNumberError as e:
        if e.word == 'stop':
            break
        else:
            print('Вы ввели не число')

print(result)
