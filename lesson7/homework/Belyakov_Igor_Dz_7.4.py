import math
import os
from collections import defaultdict


stats = {}
stats2 = defaultdict(lambda: 0)
for dirname, subdirs, filenames in os.walk('../../'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        stat = os.stat(full_path)
        size = 10 ** math.ceil(math.log(stat.st_size, 10))

        stats.setdefault(size, 0)
        stats[size] += 1

        stats2[size] += 1

print(stats)
print(stats2)
