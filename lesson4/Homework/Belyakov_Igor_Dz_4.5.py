
import sys

from utils import get_currency_rate

currencies = sys.argv[1:]
if len(currencies) > 0:
    for currency in currencies:
        currency_rate, course_date = get_currency_rate(currency)
        print(f'{currency} {currency_rate}, {course_date}')
else:
    print('Передайте набор валют через пробел в качестве аргументов для данного скрипта')
