import sys
import math

times = list()
distances = list()

with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        if line[0] == "Time:":
            #times.extend(line[1:])
            times.append("".join(line[1:]))
        if line[0] == "Distance:":
            #distances.extend(line[1:])
            distances.append("".join(line[1:]))

times = [int(x) for x in times]
distances = [int(x) for x in distances]

data = list()
for x in range(len(times)):
    dists = [y * (times[x] - y) for y in range(times[x])]
    data.append(len([y for y in dists if y > distances[x]]))

print(data)
print(math.prod(data))



