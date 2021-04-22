
from utils import get_currency_rate


for currency in ['USD', 'EUR']:
    currency_rate, course_date = get_currency_rate(currency)
    print(f'{currency} {currency_rate}, {course_date}')
