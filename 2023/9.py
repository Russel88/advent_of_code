import sys

data = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        numbers = line.strip().split()
        numbers = [int(x) for x in numbers]
        
        # Second
        #numbers = numbers[::-1]

        # Differences
        diff = [numbers, [x - y for x,y in zip(numbers[1:], numbers[:-1])]]
        while any([x != 0 for x in diff[-1]]):
            diff.append([x - y for x,y in zip(diff[-1][1:], diff[-1][:-1])])

        # Forcast
        n = 0
        last = 0
        for dd in diff[::-1]:
            last += dd[-1]

        data.append(last)

print(sum(data))
