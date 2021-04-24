
import sys
import os

if len(sys.argv) != 3:
    print('Вам надо передать номер строки и новое число')
    exit(1)

start = int(sys.argv[1])-1
if start*11 >= os.path.getsize('sales.txt'):
    print('Такой строки в файле нет')
    exit(1)

with open('sales.txt', 'r+', encoding='utf8') as f:
    f.seek(11*start)
    print(f'{sys.argv[2]:10}', file=f)
