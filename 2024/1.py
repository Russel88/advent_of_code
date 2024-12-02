import sys
from collections import Counter

data1 = list()
data2 = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        data1.append(int(line[0]))
        data2.append(int(line[1]))

data1_sorted = sorted(data1)
data2_sorted = sorted(data2)

#distance = [abs(x - y) for x, y in zip(data1_sorted, data2_sorted)]
#print(sum(distance))

counter = Counter(data2_sorted)

res = [x * counter.get(x, 0) for x in data1_sorted]
print(sum(res))