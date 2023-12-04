import sys
import regex as re

def card_reader(x):
    
    x = x.strip().split(':')
    card = x[0]
    numbers = x[1].strip().split('|')
    winning = numbers[0].strip().split()
    youhave = numbers[1].strip().split()

    winning = set([float(x) for x in winning])
    youhave = set([float(x) for x in youhave])

    wins = youhave.intersection(winning)
    
    # First
    #if len(wins) == 0:
    #    return(0)
    #else:
    #    return(int((2 ** len(wins)) / 2))

    # Second
    return(len(wins))

data = list()

copy_counter = [0]*1000
n = 0
with open(sys.argv[1]) as fh:
    for line in fh:
        
        # Second
        matching = card_reader(line)
       
        if matching > 0:
            for i in range(matching):
                copy_counter[n + i + 1] += copy_counter[n] + 1
        
        cards = copy_counter[n] + 1
        data.append(cards)

        n += 1

        # First
        # data.append(matching)

print(sum(data))
