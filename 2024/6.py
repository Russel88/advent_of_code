import sys
import numpy as np

data = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        data.append(line)

data = [list(x) for x in data]

mat = np.array(data)

# Find ^
up = np.where(mat == "^")
# To tuple
up = (up[0][0], up[1][0])

def travel_map(mat, current_position):
    positions_visited = []
    on_map = True
    rotations = 0
    while on_map:
        # Find obstacles
        obstacles = np.where(mat == "#")
        # To tuples
        obstacles = list(zip(obstacles[0], obstacles[1]))
        # Find the obstacles above current position
        obstacles_column = [x for x in obstacles if x[1] == current_position[1] and x[0] < current_position[0]]
        if len(obstacles_column) > 0:
            # Find the closest one
            obstacle = max(obstacles_column)
            # Add all positions visited
            for i in range(obstacle[0] + 1, current_position[0]):
                mat[i, current_position[1]] = "X"
            # Move to position just before obstacle
            current_position = obstacle[0] + 1, current_position[1]
            if (current_position, rotations) in positions_visited:
                # If we have been here before, we are stuck
                return []
            positions_visited.append((current_position, rotations))
            # Change direction by rotating obstacle map (we turn right by 90 degrees)
            mat = np.rot90(mat, 1)
            rotations += 1
            if rotations == 4:
                rotations = 0
            # Get position according to new map
            current_position = (len(mat) - current_position[1] - 1, current_position[0])
        else:
            # Move to edge and break
            for i in range(0, current_position[0]):
                mat[i, current_position[1]] = "X"
            on_map = False
    return mat, rotations

# Find all positions visited on original map
mat, rotations = travel_map(mat, up)
# Return map to original state
mat = np.rot90(mat, -rotations)
positions_visited = np.where(mat == "X")

# Print the result
# Count X
print(np.count_nonzero(mat == "X") + np.count_nonzero(mat == "^"))


# For each visited add an obstacle on the original map and try again
loops = 0
for i in range(len(positions_visited[0])):
    mat = np.array(data)
    mat[positions_visited[0][i], positions_visited[1][i]] = "#"
    mat = travel_map(mat, up)
    # If travel_map returns empty, we are stuck in loop, count this
    if len(mat) == 0:
        loops += 1

print(loops)
