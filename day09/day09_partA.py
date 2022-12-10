# adventOfCode 2022 day 9
# https://adventofcode.com/2022/day/9


import numpy as np
import math

def is_touching(head_location, tail_location):
    # Really it's less than sqrt(2) ~ 1.414
    if math.dist(head_location, tail_location) < 1.5:
        # return tail_location
        return True

def get_new_tail_location(head_location, tail_location):
    if is_touching(head_location, tail_location):
        return tail_location
    # If two blocks apart in any of the four directions
    # Really less than 2 (but I'm accounting for potential round-off)
    if math.dist(head_location, tail_location) < 2.1:
        return (head_location + tail_location) // 2
    for movement in [np.array([1,1]), np.array([1,-1]), np.array([-1,1]), np.array([-1,-1])]:
        new_tail_location = tail_location + movement
        if is_touching(head_location, new_tail_location):
            return new_tail_location
    raise(ValueError(f'ERROR: Cannot find new tail for given head/tail combination: {head_location}, {tail_location}'))

head_location = np.array([0,0])
tail_location = np.array([0,0])
direction_coords = {'R': np.array([1,0]), 'L': np.array([-1,0]), 'U': np.array([0,1]), 'D': np.array([0,-1])}
all_tail_points = set()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        direction, distance = in_string.split(' ')
        distance = int(distance)
        for i in range(distance):
            head_location += direction_coords[direction]
            tail_location = get_new_tail_location(head_location, tail_location)
            all_tail_points.add(tuple(tail_location))


print(f'Total number of positions visited by tail (answer to A) is {len(all_tail_points)}\n')
