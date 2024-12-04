import sys
import numpy as np

# Read data as matrix
data = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        data += [list(line)]

string = "XMAS"
mm = np.array(data)

def count_string(string, m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if ''.join(m[i][j:j+4]) == string:
                count += 1
    return count

def get_all_diagonals(m):
    nrow = len(m)
    ncol = len(m[0])
    diags = []
    for i in range(nrow):
        diags.append(list(np.diagonal(m,offset=i)))
        if i != 0:
            diags.append(list(np.diagonal(m,offset=-i)))
    return diags


def count_all(string, m):
    count = 0
    count += count_string(string, m)
    diags = get_all_diagonals(m)
    count += count_string(string, diags)
    return count

count = 0
for i in range(4):
    count += count_all(string, mm)
    mm = np.rot90(mm)

print(count)

def find_xmas(kk):
    if kk[0][0] == 'M' and kk[2][2] == 'S' and kk[2][0] == 'S' and kk[0][2] == 'M': 
        return True
    else:
        return False

# Find all A
count = 0
for i in range(len(mm)):
    for j in range(len(mm[0])):
        if mm[i][j] == 'A':
            # Get neighborhood
            kk = np.array(mm[i-1:i+2,j-1:j+2])
            if len(kk) == 3 and len(kk[0]) == 3:
                for z in range(4):
                    kk = np.rot90(kk)
                    if find_xmas(kk):
                        count += 1
            
print(count)
                    