import numpy as np
import sys

# Read matrix data
matrix = np.genfromtxt(sys.argv[1], delimiter=1, dtype=str) 

def count_tiles(matrix, start):
    positions_covered = set([start[:2]])
    positions_direct_covered = set(start)

    def new_direction(current_direction, signal):
        if signal == ".":
            return current_direction
        if signal == "R":
            if current_direction == "N":
                return "E"
            if current_direction == "E":
                return "N"
            if current_direction == "S":
                return "W"
            if current_direction == "W":
                return "S"
        if signal == "L":
            if current_direction == "N":
                return "W"
            if current_direction == "W":
                return "N"
            if current_direction == "S":
                return "E"
            if current_direction == "E":
                return "S"
        if signal == "-":
            if current_direction in ["W", "E"]:
                return current_direction
            else:
                return ["W", "E"]
        if signal == "|":
            if current_direction in ["N", "S"]:
                return current_direction
            else:
                return ["N", "S"]

    def new_position(current_position, direction):
        x, y = current_position
        if direction == "N":
            new_position = (x, y - 1)
        if direction == "E":
            new_position = (x + 1, y)
        if direction == "S":
            new_position = (x, y + 1)
        if direction == "W":
            new_position = (x - 1, y)
        return new_position

    def is_position_in_matrix(matrix, position):
        x, y = position
        if x < 0 or y < 0:
            return False
        if x >= matrix.shape[0] or y >= matrix.shape[1]:
            return False
        return True

    positions = [start]
    while len(positions) > 0:
        new_positions = []
        for position in positions:
            try:
                signal = matrix[position[1], position[0]]
            
                direct = new_direction(position[2], signal)
                if type(direct) == list:
                    for d in direct:
                        x, y = new_position(position[:2], d)
                        to_save = (x, y, d)
                        if is_position_in_matrix(matrix, to_save[:2]):
                            # Stop at visited
                            if not to_save in positions_direct_covered:
                                new_positions.append(to_save)
                                positions_covered.add(tuple(to_save[:2]))
                                positions_direct_covered.add(to_save)
                else:
                    x, y = new_position(position[:2], direct)
                    to_save = (x, y, direct)
                    if is_position_in_matrix(matrix, to_save[:2]):
                        # Stop at visited
                        if not to_save in positions_direct_covered:
                            new_positions.append(to_save)
                            positions_covered.add(tuple(to_save[:2]))
                            positions_direct_covered.add(to_save)

            except:
                pass
        positions = new_positions

    return len(positions_covered)

# Loop over all possible starts
## All eastward starts
eastward_starts = [(0, x, "E") for x in range(matrix.shape[1])]
## All westward starts
westward_starts = [(matrix.shape[0] - 1, x, "W") for x in range(matrix.shape[1])]
## All northward starts
northward_starts = [(x, 0, "S") for x in range(matrix.shape[0])]
## All southward starts
southward_starts = [(x, matrix.shape[1] - 1, "N") for x in range(matrix.shape[0])]

# Count tiles for all starts
eastward_counts = [count_tiles(matrix, x) for x in eastward_starts]
westward_counts = [count_tiles(matrix, x) for x in westward_starts]
northward_counts = [count_tiles(matrix, x) for x in northward_starts]
southward_counts = [count_tiles(matrix, x) for x in southward_starts]

# Print the maximum
print(count_tiles(matrix, (0, 0, "E")))
print(max(eastward_counts + westward_counts + northward_counts + southward_counts))