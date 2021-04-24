result = {}
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        elements = line.split()
        ip = elements[0]
        result.setdefault(ip, 0)
        url = elements[6]
        result[ip] += 1
max_ip = None
max_count = 0
for ip, cnt in result.items():
    if cnt > max_count:
        max_ip = ip
        max_count = cnt

print('spammer', max_ip, max_count)
