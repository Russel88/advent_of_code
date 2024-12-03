import sys
import re

data = ''
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        data += line

#test = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)
test = re.findall(r'((?:mul\([0-9]{1,3},[0-9]{1,3}\))|(?:do(?:n\'t)?\(\)))', data)

print(test)
def mult_numbers(x):
    x = re.findall(r'[0-9]{1,3}', x)
    return int(x[0]) * int(x[1])

#multed = [mult_numbers(x) for x in test] 
#print(sum(multed))

res = 0
included = True
for x in test:
    if x.startswith('mul'):
        if included:
            res += mult_numbers(x)
    elif x.startswith('don'):
        included = False
    elif x.startswith('do'):
        included = True
    else:
        print('error')

print(res)