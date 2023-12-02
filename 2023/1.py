import sys
import regex as re

data = list()
with open(sys.argv[1]) as fh:
    for line in fh:
        data.append(line.strip())

def find_number(x):
    i = r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)'
    test = re.findall(i, x, overlapped = True)

    if test[0].isnumeric():
        test1 = test[0]
    else:
        test1 = number_dict[test[0]]
    if test[-1].isnumeric():
        test2 = test[-1]
    else:
        test2 = number_dict[test[-1]]

    return(int(str(test1)+str(test2)))

number_dict = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9}


numbers = [find_number(x) for x in data]

print(sum(numbers))

