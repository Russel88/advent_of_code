import sys
import networkx as nx

rules = []
prints = []

rule = True
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        if line == "":
            rule = False
            continue
        if rule:
            rules.append(line)
        else:
            prints.append(line)

rules = [x.split("|") for x in rules]
prints = [x.split(",") for x in prints]

rules = [[int(y) for y in x] for x in rules]
prints = [[int(y) for y in x] for x in prints]

def check_rule(ll, rules):
    ok = True
    for n, y in enumerate(ll):
        # First we check that every element after abides by the rules
        current_rules = [x[0] for x in rules if x[1] == y]
        if len(ll) > n+1 and len(current_rules) > 0:
            if any([x in current_rules for x in ll[n+1:]]):
                ok = False
                break
        # Then we check that every element before abides by the rules
        current_rules = [x[1] for x in rules if x[0] == y]
        if n > 0 and len(current_rules) > 0:
            if any([x in current_rules for x in ll[:n]]):
                ok = False
                break
    return ok

def fix_wrong_orders(ll, rules):
    ll_new = ll
    for n, y in enumerate(ll):
        # First we check that every element after abides by the rules
        current_rules = [x[0] for x in rules if x[1] == y]
        if len(ll) > n+1 and len(current_rules) > 0:
            for x in current_rules:
                if x in ll[n+1:]:
                    # Pull it out and put it in the front
                    ll_new.remove(y)
                    ll_new.insert(ll_new.index(x) + 1, y)
        # Then we check that every element before abides by the rules
        current_rules = [x[1] for x in rules if x[0] == y]
        if n > 0 and len(current_rules) > 0:
            for x in current_rules:
                if x in ll[:n]:
                    # Pull it out and put it in the back
                    ll_new.remove(y)
                    ll_new.insert(ll_new.index(x), y)
    # Keep doing this until the list is sorted correctly
    while not check_rule(ll_new, rules):
        ll_new = fix_wrong_orders(ll_new, rules)
    return ll_new

def get_middle_number(ll, ok):
    #if not ok:
    #    return 0
    #return ll[len(ll) // 2]
    if ok:
        return 0
    updated = fix_wrong_orders(ll, rules)
    return updated[len(updated) // 2]

# Topological sort - does not work
# Turn rules into directed graph
graph = nx.DiGraph()
for i in rules:
    graph.add_edge(i[0], i[1])
# rules_order = list(nx.topological_sort(graph))
# print(rules_order)

print(sum([get_middle_number(x, check_rule(x, rules)) for x in prints]))