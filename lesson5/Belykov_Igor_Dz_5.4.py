src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [cv for ipe, cv in enumerate(src[1:]) if src[ipe] < cv]
print(src)
print(result)
