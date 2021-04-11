def thesaurus(*args):
    dictionary = {}
    for name in args:
        first_letter = name[0]
        dictionary.setdefault(first_letter, [])
        dictionary[first_letter].append(name)
    return dictionary


d = thesaurus("Иван", "Мария", "Петр", "Илья")
for first_letter in sorted(d.keys()):
    print(f'{first_letter}: {d[first_letter]}')

# Подумайте: полезен ли будет вам оператор распаковки?   нет
# Сможете ли вы вернуть отсортированный по ключам словарь?    нет
