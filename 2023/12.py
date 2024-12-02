import sys
import itertools
import re

def combi(x, n):
    #new = [[0]*len(x)]
    #for ii in range(len(x)):
    #    if x[ii] == '.':
    #        continue
    #    if x[ii] == '#':
    #        for ii2 in range(len(new)):
    #            new[ii2][ii] = 1
    #    if x[ii] == '?':
    #        for ii2 in range(len(new)):
    #            tmp = new[ii2][:]
    #            tmp[ii] = 1
    #            new.append(tmp)
    

    certain = x.count('#')
    remain = n - certain

    scaffold = [0] * len(x)
    quest = list()
    for ii in range(len(x)):
        if x[ii] == '#':
            scaffold[ii] = 1
        if x[ii] == '?':
            quest.append(ii)

    new = list()
    potential = itertools.combinations(quest, remain)
    for ii in potential:
        tmp = scaffold.copy()
        for jj in ii:
            tmp[jj] = 1
        new.append(tmp)

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
        numbers = numbers * 5
        pattern = pattern + '?' + pattern + '?' + pattern + '?' + pattern + '?' + pattern
        print(pattern)
        
        combinations = sum([check(x, numbers) for x in combi(pattern, n = sum(numbers))])
        print(combinations)
        data.append(combinations)

print(sum(data))
