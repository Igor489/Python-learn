import json
import math
import os
from collections import defaultdict


stats2 = defaultdict(lambda: [0, set()])
for dirname, subdirs, filenames in os.walk('../../'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        stat = os.stat(full_path)
        size = 10 ** math.ceil(math.log(stat.st_size, 10))
        stats2[size][0] += 1
        segments = filename.split('.')
        if len(segments) > 1:
            ext = segments[-1]
        else:
            ext = ''
        stats2[size][1].add(ext)

stat = {k: (v[0], list(v[1])) for k, v in stats2.items()}
print(stat)

base_name = os.path.basename(os.path.abspath('.'))
filename = f'{base_name}_summary.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(stat, f, indent=4)
