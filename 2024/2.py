import sys

data = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        data.append([int(x) for x in line])

def remove_one(k, i):
    z = k[:i] + k[i+1:]
    return is_increasing_or_decreasing(z)

def is_increasing_or_decreasing(x):
    shifted = x[-1:] + x[:-1]
    diff = [z - y for z, y in zip(x, shifted)]
    diff = diff[1:]
    if all([z > 0 and z <= 3 for z in diff]):
        return True
    if all([z < 0 and z >= -3 for z in diff]):
        return True
    return False

def loop_over_index(k):
    for i in range(len(k)):
        if remove_one(k, i):
            return True
    return False

print(sum([is_increasing_or_decreasing(x) for x in data]))
print(sum([loop_over_index(x) for x in data]))
