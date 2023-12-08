import sys
import re
import math

n = 0
network = dict()
with open(sys.argv[1]) as fh:
    for line in fh:
        if n == 0:
            n += 1
            direction = line.strip()
            continue

        if n == 1:
            n += 1
            continue

        line = line.strip().split(' = ')
        network[line[0]] = [re.sub('[()]', '', x) for x in line[1].split(', ')]

direction = [0 if x == 'L' else 1 for x in direction]

# Try LCM
def n_steps(node):
    steps = 0
    nodeend = 'A'
    while nodeend != 'Z':
        pos = steps
        while pos >= len(direction):
            pos = pos - len(direction)
        where = direction[pos]

        node = network[node][where]
        nodeend = node[2]

        steps += 1

    return(steps)
    

current = [k for k in network if k[2] == 'A']

step_count = [n_steps(x) for x in current]

print(math.lcm(*step_count))

