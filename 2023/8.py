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
def n_steps(node, rounds = 1):
    steps = 0
    nodeend = 'A'
    while nodeend != 'Z' and rounds >= 1:
        pos = steps
        while pos >= len(direction):
            pos = pos - len(direction)
        where = direction[pos]

        node = network[node][where]
        nodeend = node[2]

        if nodeend == 'Z':
            rounds -= 1
            nodeend = 'A'

        steps += 1

    return(steps)
    

current = [k for k in network if k[2] == 'A']

step_count1 = [n_steps(x, 1) for x in current]
step_count2 = [n_steps(x, 2) for x in current]

print([x/y for x,y in zip(step_count2, step_count1)])

print(math.lcm(*step_count1))

