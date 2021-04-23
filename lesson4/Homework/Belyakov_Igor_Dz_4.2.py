import requests


def get_currency_rate(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if resp.status_code != 200:  # Ok
        print('Данные с сайта ЦБ РФ не доступны')
        exit()
    content = resp.content.decode('windows-1251')

    parts = content.split('</Valute><Valute')
    currency_code = '<CharCode>' + currency.upper() + '</CharCode>'
    for part in parts:
        if currency_code in part:
            break
    else:
        return None

    currency_rate = float(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

    return currency_rate


for currency in ['USD', 'eur']:
    print(currency, get_currency_rate(currency))
