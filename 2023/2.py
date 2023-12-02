import sys
import math



def reader(line):
    line = line.strip().split(':')
    game = int(line[0].split()[1])
    
    red = 0
    blue = 0
    green = 0

    for x in line[1].split(';'):
        x = x.strip()
        for y in x.split(','):
            y = y.strip().split()
            if y[1] == 'red':
                red = max(red, int(y[0]))
            if y[1] == 'blue':
                blue = max(blue, int(y[0]))
            if y[1] == 'green':
                green = max(green, int(y[0]))
    
    return(game, {'red': red, 'green': green, 'blue': blue})

def tester(dct, red, green, blue):
    if dct['red'] <= red and dct['green'] <= green and dct['blue'] <= blue:
        return(True)
    else:
        return(False)

def proder(dct):
    return(math.prod([dct['red'],dct['green'],dct['blue']]))


data = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        game, line_dict = reader(line)

        # Challenge 1
        #if tester(line_dict, red = 12, green = 13, blue = 14):
        #    data.append(game)

        # Challenge 2
        data.append(proder(line_dict))


print(sum(data))


