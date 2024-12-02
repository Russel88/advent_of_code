import sys
import re
from collections import OrderedDict

data = list()

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        data.extend(line.strip().split(','))

def hash(s):
    v = 0
    for x in s:
        v += ord(x)
        v *= 17
        v %= 256
    return(v)

#print(sum([hash(x) for x in data]))


labels = [re.sub('[-=].*', '', x) for x in data]
values = [hash(x) for x in labels]
focals = [re.sub('.*[-=]', '', x) for x in data]
focals = [int(x) if len(x) > 0 else -1 for x in focals]


boxes = OrderedDict()

for l,v,f in zip(labels, values, focals):
    if f == -1:
        if v in boxes:
            if l in boxes[v]:
                del boxes[v][l]
    else:
        if v in boxes:
            if l in boxes[v]:
                boxes[v][l] = f
            else:
                boxes[v][l] = f
        else:
            boxes[v] = OrderedDict()
            boxes[v][l] = f


power = list()
for v in boxes:
    n = 1
    for l in boxes[v]:
        power.append((v+1) * n * boxes[v][l])
        n += 1

print(power)
print(sum(power))
