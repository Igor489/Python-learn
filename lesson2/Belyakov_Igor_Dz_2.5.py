prices = [
    10.13, 25.78, 95.12, 35.78, 83.7, 12.25, 33.93, 87.12, 79.78, 44.01,
    32.23, 52.98, 59.12, 19.78, 7.00, 3.23, 11.9, 79.55, 39.47, 60.90
]

print(id(prices))
prices.sort()
print(id(prices))

prices_to_print = []
for price in prices:
    rubles = int(price)
    kopecks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopecks:02} коп')
print(', '.join(prices_to_print))

print('-------')

new_prices = sorted(prices, reverse=True)
prices_to_print = []
print(id(new_prices))
for price in new_prices:
    rubles = int(price)
    kopecks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopecks:02} коп')
print(', '.join(prices_to_print))

print('-------')

prices_to_print = []
for price in prices[-5:]:
    rubles = int(price)
    kopecks = int(price * 100) % 100
    prices_to_print.append(f'{rubles} руб {kopecks:02} коп')
print(', '.join(prices_to_print))
