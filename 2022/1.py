import sys

data = []
index = 0
with open(sys.argv[1]) as fh:
    for line in fh:
        lime = line.strip()

        if len(data) == 0:
            data = [[int(line)]]
        
        if line == "\n":
            index += 1
            continue
        
        if len(data) == index:
            data.append([])
        data[index].append(int(line))


summed = [sum(x) for x in data]

# First
# print(max(summed))

# Second
sum_ordered = sorted(summed)
print(sum(sum_ordered[-3:]))

        

