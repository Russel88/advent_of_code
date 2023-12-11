import sys
import numpy as np
import cv2

sys.setrecursionlimit(100000)

# Kernels
kernels = {'S': np.asarray([[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
           '-': np.asarray([[0, 0, 0], [1, 0, 1], [0, 0, 0]]),
           '|': np.asarray([[0, 1, 0], [0, 0, 0], [0, 1, 0]]),
           'F': np.asarray([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
           'L': np.asarray([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
           '7': np.asarray([[0, 0, 0], [1, 0, 0], [0, 1, 0]]),
           'J': np.asarray([[0, 1, 0], [1, 0, 0], [0, 0, 0]])}

# Neighborhood finder
def subarray_from_kernel(a, a_kernel, i, j):
    return(np.where(a_kernel, a[(j-1):(j+2), (i-1):(i+2)], 0))

# Loop finder
def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths

# Load matrix
matrix = np.genfromtxt(sys.argv[1], delimiter=1, dtype=str)
matrix = np.pad(matrix, ((1,1), (1,1)), constant_values = '.')
height, width = matrix.shape

graph = dict()
# For each position fill edges
for i in range(1, (width - 1)):
    for j in range(1, (height - 1)):

        node = str(i)+','+str(j)
        graph[node] = list()
        
        if matrix[j, i] == '.':
            continue

        kernel = kernels[matrix[j, i]]
        subarray = subarray_from_kernel(matrix, kernel, i, j)

        if subarray[0, 1] in ('S', '|', 'F', '7'):
            graph[node].append(str(i)+','+str(j-1))
        if subarray[1, 0] in ('S', '-', 'F', 'L'):
            graph[node].append(str(i-1)+','+str(j))
        if subarray[1, 2] in ('S', '-', '7', 'J'):
            graph[node].append(str(i+1)+','+str(j))
        if subarray[2, 1] in ('S', '|', 'J', 'L'):
            graph[node].append(str(i)+','+str(j+1))

# Find cycles
ii = np.where(matrix == 'S')
S = str(ii[1][0])+','+str(ii[0][0])
cycles = DFS(graph, S)

longest = max([len(x) for x in cycles])

# First
#print(len([x for x in cycles if len(x) == longest][0]) // 2)

# Second
path = [x for x in cycles if len(x) == longest][0]
new = np.zeros(matrix.shape)

n = 1
for node in path:
    i, j = node.split(',')
    new[int(j), int(i)] = 1
    n += 1

def find_enclosed(array, enh = False):
    binary = np.where(array > 0, 1, 0).astype(np.uint8)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    height, width = array.shape

    enclosed = list()
    for i in range(width):
        for j in range(height):
            test = cv2.pointPolygonTest(contours[0], (i,j), False)
            if test == 1:
                node = str(i)+','+str(j)
                if enh:
                    enclosed.append((i, j))
                else:
                    if node not in path:
                        enclosed.append((i, j))

    return(enclosed)

enclosed_original = find_enclosed(new)

# Enhance
enhanced = np.zeros((height*2, width*2))
for i in range(width):
    for j in range(height):
        node = str(i)+','+str(j)
        if node in path:
            enhanced[j*2, i*2] = 1
            if str(i+1)+','+str(j) in graph[node]:
                enhanced[j*2, i*2+1] = 1
            if str(i)+','+str(j+1) in graph[node]:
                enhanced[j*2+1, i*2] = 1
            if str(i+1)+','+str(j+1) in graph[node]:
                enhanced[j*2+1, i*2+1] = 1

enclosed_enhanced = find_enclosed(enhanced, True)

# Only get the original ones
enclosed_enhanced_sub = [x for x in enclosed_enhanced if x[0] % 2 == 0 and x[1] % 2 == 0]

# Count which in the enhanced enclosed are in the original enclosed
count = 0
for x in enclosed_enhanced_sub:
    potential = (x[0]//2, x[1]//2)
    if potential in enclosed_original:
        count += 1

print(count)
