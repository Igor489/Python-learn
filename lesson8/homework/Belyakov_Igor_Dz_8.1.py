import re

re_email = re.compile('^([a-zA-Z0-9_.-]+)@((([a-zA-Z0-9-]+)\.)+[a-zA-Z]+)$')


def email_parse(email):
    match = re_email.match(email)
    if match:
        return {'username': match.group(1), 'domain': match.group(2)}
    else:
        raise ValueError('некорректный email-адрес')


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
