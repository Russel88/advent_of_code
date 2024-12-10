import sys
import itertools

data = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split(":")
        data.append((int(line[0]), [int(x) for x in line[1].strip().split()])) 

def add_or_mult(ll, mult):
    result = ll[0]
    for i in range(len(ll) - 1):
        if mult[i]:
            result = result * ll[i + 1]
        else:
            result = result + ll[i + 1]
    return result

def add_mult_or_concat(ll, mult):
    result = ll[0]
    for i in range(len(ll) - 1):
        if mult[i] == 0:
            result = result + ll[i + 1]
        elif mult[i] == 1:
            result = result * ll[i + 1]
        else:
            result = int(str(result) + str(ll[i + 1]))
    return result

def mult_combinations(ll):
    #for comb in itertools.product([True, False], repeat = len(ll) - 1):
    for comb in itertools.product([0, 1, 2], repeat = len(ll) - 1):
        #yield add_or_mult(ll, comb)
        yield add_mult_or_concat(ll, comb)

total_cali = 0
for d in data:
    for comb in mult_combinations(d[1]):
        if comb == d[0]:
            print(comb)
            total_cali += comb
            break

print(total_cali)
