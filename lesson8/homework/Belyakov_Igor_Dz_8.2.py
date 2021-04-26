import re


re_log = re.compile(r'^((\d+\.){3}\d+) - - \[([^]]+)\] "([^ ]+) ([^ ]+) [^"]*" (\d+) (\d+) .*$')

with open('../../lesson6/homework/nginx_logs.txt', 'r', encoding='utf-8') as f:
    for n, line in enumerate(f):
        match = re_log.match(line)
        if match:
            remote_addr = match.group(1)
            request_datetime = match.group(3)
            request_type = match.group(4)
            requested_resource = match.group(5)
            response_code = int(match.group(6))
            response_size = int(match.group(7))

            result = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)

            print(result)
        if n > 10:
            break
