import sys
import jellyfish

def distance(x, y):
    if x == None or y == None:
        return(None)
    if jellyfish.levenshtein_distance(x, y) < 2:
        return(jellyfish.levenshtein_distance(x, y))
    else:
        return(None)

def list_similar(x, y):
    dd = [distance(k1, k2) for k1,k2 in zip(x, y)]
    if any([x is None for x in dd]):
        return(False)
    if sum([x for x in dd if x is not None]) == 1:
        return(True)
    else:
        return(False)


def find_reflect(lst):
    potential = list()

    prev = None
    n = 0
    for x in lst:
        if distance(x, prev) is not None:
            potential.append(n)
        prev = x
        n += 1
    return(potential)

def mirror_check(lst, pos):
    
    if len(pos) == 0:
        return(False)

    reflect = [min(x, len(lst) - (x)) for x in pos]
    check = [list_similar(lst[(x-y):(x)][::-1], lst[(x):(x+y)]) for x,y in zip(pos, reflect)]
    
    ok = [(x, z) for x,y,z in zip(pos, check, reflect) if y]
    
    if len(ok) > 0:
        largest = max([x[1] for x in ok])
        this = [x[0] for x in ok if x[1] == largest][0]
        return(this)
    else:
        return(False)


def mirror(a):
    rows = [''.join(x) for x in a]
    cols = [''.join([y[x] for y in a]) for x in range(len(a[0]))]
   
    row_left = find_reflect(rows)
    col_up = find_reflect(cols)

    row_check = mirror_check(rows, row_left)
    col_check = mirror_check(cols, col_up)

    if row_check:
        return(100*(row_check))
    elif col_check:
        return(col_check)

data = list()
with open(sys.argv[1]) as fh:
    mat = list()
    for line in fh:
        if len(line.strip()) == 0:
            data.append(mirror(mat))
            mat = list()
            continue
        mat.append(line.strip())
    data.append(mirror(mat))

print(sum(data))
