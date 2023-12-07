import sys
from collections import Counter
import re

#cards = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
cards = {'A': 1, 'K': 2, 'Q': 3, 'J': 14, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
types = {'Five': 1, 'Four': 2, 'House': 3, 'Three': 4, 'Pairs': 5, 'Pair': 6, 'High': 7}

def hand_score(this):
    y = Counter(this)
    
    # Second
    ## Replce J's with the most common, unless all are J's
    if 'J' in y:
        if len(y) > 1:
            no_joker = Counter({k: v for k, v in y.items() if k != 'J'})
            most_common = no_joker.most_common(1)[0][0]
            this = this.replace('J', most_common)
            y = Counter(this)
     
    if len(y) == 1:
        handtype = 'Five'
    if len(y) == 2:
        if any([True for x in y.values() if x == 4]):
            handtype = 'Four'
        else:
            handtype = 'House'
    if len(y) == 3:
        if any([True for x in y.values() if x == 3]):
            handtype = 'Three'
        else:
            handtype = 'Pairs'
    if len(y) == 4:
        handtype = 'Pair'
    if len(y) == 5:
        handtype = 'High'

    score = types[handtype]
    return([score])

def translate(this):
    out = list()
    for x in this:
        out.append(cards[x])
    return(out)

scores = list()
bids = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip().split()
        scores.append(hand_score(line[0]) + translate(line[0]))
        bids.append(int(line[1]))

final = list(zip(scores, bids))

# Sort by card strength
iteration = 5
while iteration > -1:
    final = sorted(final, key=lambda x: x[0][iteration])
    iteration -= 1

# Reverse list and add ranks
final = list(zip([x[1] for x in final[::-1]], list(range(len(final)))))
print(sum([x[0]*(x[1]+1) for x in final]))
