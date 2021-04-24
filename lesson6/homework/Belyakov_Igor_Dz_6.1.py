result = []
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        elements = line.split()
        ip = elements[0]
        method = elements[5][1:]
        url = elements[6]
        result.append((ip, method, url))

# print(result[:10])
# print(len(result))
