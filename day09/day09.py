# adventOfCode 2022 day 9
# https://adventofcode.com/2022/day/9


import numpy as np
head_location = np.array([0,0])
direction_coords = {'R': np.array([1,0]), 'L': np.array([-1,0]), 'U': np.array([0,1]), 'D': np.array([0,-1])}

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string, end = ': ')
        direction, distance = in_string.split(' ')
        distance = int(distance)
        for i in range(distance):
            head_location += direction_coords[direction]
            print(head_location, end = ', ')
        print()
print()

