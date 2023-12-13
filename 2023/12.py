import sys
import itertools

def combi(x, n=None):
    new = [[0]*len(x)]
    for ii in range(len(x)):
        if x[ii] == '.':
            continue
        if x[ii] == '#':
            for ii2 in range(len(new)):
                new[ii2][ii] = 1
        if x[ii] == '?':
            for ii2 in range(len(new)):
                tmp = new[ii2][:]
                tmp[ii] = 1
                new.append(tmp)
    
    if n is not None:
        orig = new[:]
        for y in range(n - 1):
            for ii2 in range(len(new)):
                new.append(new[ii2][:] + [1])
                new.append(new[ii2][:] + [0])
                
            new = [x[0] + x[1] for x in itertools.product(new, orig)]
            # Separately for 0 and 1 take the new lists and add the orig lists to them in the same order then combine the 0 and 1 new lists 

    return(new)


def check(pp, nn):
    if sum(pp) != sum(nn):
        return(False)
    pp_split = [y for y in ''.join([str(x) for x in pp]).split('0') if len(y) > 0]
    if len(pp_split) != len(nn):
        return(False)
    if all([x == y for x, y in zip([len(x) for x in pp_split], nn)]):
        return(True)
    else:
        return(False)

data = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        
        pattern = line[0]
        numbers = [int(x) for x in line[1].split(',')]

        # First
        #combinations = sum([check(x, numbers) for x in combi(pattern)])
        #data.append(combinations)
        
        # Second
        numbers = numbers * 3
        
        combinations = sum([check(x, numbers) for x in combi(pattern, n=3)])
        print(combinations)
        data.append(combinations)

print(sum(data))
