"""
Goal: Within matrix m*n with positive numbers need to find the longest
path increasing numbers sequence. Path can go right, left, up, down.

Assume that in matrix no repeated numbers placed close to each other.

In ver.2 introduced caching of founded paths. This reduces recalculating.
"""

from copy import *

matrix = [[5, 47, 45, 7], [6, 8, 13, 21], [4, 9, 11, 19]]

memo = [[0] * len( matrix[0] ) for _ in range( len(matrix) )]  # for caching paths

steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def simulate_journey(x, y):
    if memo[x][y] != 0:
        return memo[x][y]

    found_path = []
    for step in steps:
        path = []  # value + direction to next
        new_position = (x + step[0], y + step[1])

        # check if we still in bounds of matrix
        if new_position[0] < 0:
            continue
        if new_position[0] >= len(matrix):
            continue
        if new_position[1] < 0:
            continue
        if new_position[1] >= len(matrix[0]):
            continue

        cur_val = matrix[x][y]
        candidate_value = matrix[new_position[0]][new_position[1]]
        if cur_val < candidate_value:
            print('{0} -> {1}'.format(cur_val, candidate_value))
            path.append((cur_val, step))
            simulated = simulate_journey(new_position[0], new_position[1])
            if len(simulated) > 0:
                path = path + simulated
            else:
                path.append((candidate_value, (0, 0)))  # found the largest number in this path

            print(path)

        if len(path) > len(found_path):
            found_path = deepcopy(path)

    if len(found_path) > 0:
        memo[x][y] = found_path
    return found_path


longest_path = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        simulated_path = simulate_journey(i, j)
        if len(simulated_path) >= len(longest_path):
            longest_path = deepcopy(simulated_path)

print('longest_path')
print(longest_path)

