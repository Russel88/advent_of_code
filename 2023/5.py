import sys

seeds = list()
maps = dict()
in_map = False
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        if len(line) == 0:
            in_map = False
        else:
            if line[0] == 'seeds:':
                seeds = [int(x) for x in line[1:]]
            if not in_map:
                if line[1] == 'map:':
                    map_type = line[0]
                    maps[map_type] = []
                    in_map = True
            else:
                maps[map_type].append([int(x) for x in line])

def map_handler1(maptype, source):
    dct = maps[maptype]

    destination = source
    
    for row in dct:
        if source >= row[1] and source <= row[1] + row[2]:
            destination = source - row[1] + row[0]
            break

    return(destination)

def map_handler2(maptype, source_list):
    # Input is a list of (start, end) tuples
    dct = maps[maptype]

    dest_list = list()

    for source in source_list:
        overlaps = []
        for row in dct:
            # Source is overlapping with map
            if source[0] <= row[1] + row[2] - 1 and source[1] >= row[1]:
                overlap = (max(source[0], row[1]), min(source[1], row[1] + row[2] - 1))
                overlaps.append(overlap)

                destination = (row[0] + overlap[0] - row[1], row[0] + overlap[1] - row[1])
                dest_list.append(destination)
        # In the end also save the non-overlapping intervals
        if len(overlaps) > 0:
            min_overlap = min([x[0] for x in overlaps])
            max_overlap = max([x[1] for x in overlaps])
            if source[0] < min_overlap:
                destination = (source[0], min_overlap - 1)
                dest_list.append(destination)
            if source[1] > max_overlap:
                destination = (max_overlap + 1, source[1])
                dest_list.append(destination)
        else:
            dest_list.append(source)
    
    return(dest_list)

def map_iter(seed, map_dct = maps):
    dct_next = {x.split('-')[0]: x.split('-')[2] for x in map_dct.keys()}
    dct_key = {x.split('-')[0]: x for x in map_dct.keys()}

    ok = True
    name = 'seed'
    key_name = 'seed-to-soil'
    destination = seed

    while ok:
        try:
            #destination = map_handler1(key_name, source = destination)
            destination = map_handler2(key_name, source_list = destination)
            name = dct_next[name]
            key_name = dct_key[name]
        except KeyError:
            ok = False

    return(destination)

# First
#print(min([map_iter(maps, x) for x in seeds]))

# Second
seeds = [[(x[0], x[0]+x[1]-1)] for x in list(zip(seeds[::2], seeds[1::2]))]

print(min([min([y[0] for y in map_iter(x)]) for x in seeds]))
