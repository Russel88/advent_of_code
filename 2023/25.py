import sys
import regex as re
import random
import networkx as nx

g = nx.Graph()

with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        line = line.split(": ")
        node = line[0]
        neighbors = line[1].split(" ")
        for neighbor in neighbors:
            g.add_edge(node, neighbor)

print(g)

ebc = nx.edge_betweenness_centrality(g)

gg = g.copy()
while True:
    # Remove 3 random edges weighted by betweenness centrality
    these_edges = random.choices(list(ebc.keys()), weights=ebc.values(), k=3)
    for edge in these_edges:
        try:
            g.remove_edge(*edge)
        except:
            continue
    # Get connected component sizes
    sizes = [len(x) for x in nx.connected_components(g)]
    if len(sizes) == 2:
        print(sizes)
        print(sizes[0] * sizes[1])
        break
    else:
        g = gg.copy()

