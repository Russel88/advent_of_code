import sys
import numpy as np
import re

with open(sys.argv[1]) as fh:
    mat = list()
    for line in fh:
        mat.append(line.strip())
    cols = [''.join([y[x] for y in mat]) for x in range(len(mat[0]))]


# First
#sections = [x.split('#') for x in cols]
#cubes = [[-1]+[y for y in range(len(x)) if x[y] == '#'] for x in cols]

#section_count = [[y.count('O') for y in x] for x in sections]

#coln = len(cols[0])
#sums = [sum([sum([coln-k for k in range(v+1, v+1+z)]) for z,v in zip(x,y)]) for x,y in zip(section_count, cubes)]

#print(sums)
#print(sum(sums))

# Second
aa = np.array([list(x) for x in cols])

def flip(a):
    
    sections = [''.join(x).split('#') for x in a]
    cubes = [[-1]+[y for y in range(len(x)) if x[y] == '#'] for x in a]
    section_count = [[y.count('O') for y in x] for x in sections]

    coln = len(cols[0])
    
    a[a == 'O'] = '.'
    column = 0
    for x,y in zip(section_count, cubes):
        for z,v in zip(x,y):
            if z > 0:
                for k in range(v+1, v+1+z):
                    a[column, k] = 'O'
        column += 1

    return(a)

nn = list()

cycle = 0
while cycle < 4 * 1000:
    
    if (cycle + 1) % 4 == 0:
        coln = aa.shape[0]
        sums = [np.sum([coln-y for y in np.where(x == 'O')]) for x in np.rot90(aa)]
        nn.append(str(sum(sums)))

    aa = flip(aa)
    cycle += 1
    aa = np.rot90(aa, axes = (0, 1))

    if cycle % 100 == 0:
        regex = re.compile(r'(.+ .+)( \1)+')
        match = regex.search(' '.join(nn))
        try:
            mm = match.group(1).split()
            print(mm[((1000000000-2-match.start())%len(mm))-len(mm)-2])
        except AttributeError:
            pass
        
