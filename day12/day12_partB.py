# adventOfCode 2022 day 12
# https://adventofcode.com/2022/day/12


import numpy as np
import math
import sys

height_map = []
distance_map = []
next_positions = []


def acceptable(distance_map, height_map, position_now, potential_new_position):
    # Detect if the new potential position is off of the map
    if potential_new_position[0] < 0:
        return False
    if potential_new_position[1] < 0:
        return False
    if potential_new_position[0] >= len(distance_map):
        return False
    if potential_new_position[1] >= len(distance_map[0]):
        return False
    # The new potential position is now proven to be on the map
    
    old_height = height_map[position_now[0]][position_now[1]]
    new_height = height_map[potential_new_position[0]][potential_new_position[1]]
    if new_height == 'S':
        new_height = 'a'
    if old_height == 'E':
        old_height = 'z'

    # Fail if it has been visited before
    if not math.isinf(distance_map[potential_new_position[0]][potential_new_position[1]]):
        return False

    # OLD ... Fail if new height is more than one greater than the old height ... REPLACED BY ...
    # OLD ... Fail if old height is more than one greater than the new height
    if (ord(new_height) - ord(old_height)) < -1:
        return False
    
    # None of the failures have been triggered, so it's good
    return True

def set_distance_map(distance_map, old_position, new_position):
    distance_map[new_position[0]][new_position[1]] = distance_map[old_position[0]][old_position[1]] + 1
        
# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        if 'E' in in_string:
            next_positions.append(np.array([line_num, in_string.find('E')]))
        height_map.append(list(in_string))
        distance_map.append([float('inf')]*len(in_string))
distance_map[next_positions[0][0]][next_positions[0][1]] = 0

while True:
    position_now = next_positions.pop(0)
    for direction in [np.array([0,1]), np.array([0,-1]), np.array([1,0]), np.array([-1,0])]:
        potential_new_position = position_now + direction
        if acceptable(distance_map, height_map, position_now, potential_new_position):
            set_distance_map(distance_map, position_now, potential_new_position)
            # if problem solved
            if height_map[potential_new_position[0]][potential_new_position[1]] in ['S','a']:
                print(f'Fewest steps from E to S (modified part A) is: {distance_map[potential_new_position[0]][potential_new_position[1]]}\n')
                sys.exit('Program completed successfully')
            next_positions.append(potential_new_position)
    
