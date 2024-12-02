import sys


translate1 = {'A': "Rock", 'B': "Paper", 'C': "Scissors"}
#translate2 = {'X': "Rock", 'Y': "Paper", 'Z': "Scissors"}
points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

def get_winner(me, opponent):
    if me == opponent:
        return 1
    if me == 'Rock':
        return 2 if opponent == 'Scissors' else 0
    if me == 'Paper':
        return 2 if opponent == 'Rock' else 0
    if me == 'Scissors':
        return 2 if opponent == 'Paper' else 0

def get_shape(opponent, result):
    # X is lose, Y is draw, Z is win
    if result == "X":
        return 'Scissors' if opponent == 'Rock' else 'Rock' if opponent == 'Paper' else 'Paper'
    if result == "Y":
        return opponent
    if result == "Z":
        return 'Paper' if opponent == 'Rock' else 'Scissors' if opponent == 'Paper' else 'Rock'

def get_points(me, opponent):
    point_status = points[me]
    win_status = get_winner(me, opponent)
    point_status += win_status * 3
    return point_status

def get_points2(opponent, result):
    me = get_shape(opponent, result)
    point_status = points[me]
    win_status = get_winner(me, opponent)
    point_status += win_status * 3
    return point_status

data = []
with open(sys.argv[1]) as fh:
    for line in fh:
        lime = line.strip().split()

        #data.append(get_points(translate2[lime[1]], translate1[lime[0]]))
        data.append(get_points2(translate1[lime[0]], lime[1]))

print(sum(data))