src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
for element in src:
    if src.count(element) == 1:
        result.append(element)

print(result)

# Вариант 2

result = [element for element in src if src.count(element) == 1]
print(result)

# Вариант 3

quantity = {}
for element in src:
    quantity.setdefault(element, 0)
    quantity[element] += 1

result = []
for element in src:
    if quantity[element] == 1:
        result.append(element)

print(result)
