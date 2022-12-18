# adventOfCode 20xy day 17
# https://adventofcode.com/20xy/day/17

import numpy as np


input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    JET_PATTERN = f.readline().rstrip()
    if len(JET_PATTERN) < 50:
        print(JET_PATTERN)
    else:
        print(f'The input file is too long to print it out.  Length = {len(JET_PATTERN)}')
print()


# Coordinates of each rock are defined with respect to bottom left corner
ROCK_COLLECTION = [
    # "dash"
    [  
        np.array([0,0]),
        np.array([0,1]),
        np.array([0,2]),
        np.array([0,3])
    ],

    # "plus sign"
    [  
        np.array([1,0]),
        np.array([0,1]),
        np.array([1,1]),
        np.array([1,2]),
        np.array([2,1])
    ],

    # "backwards L"
    [  
        np.array([0,0]),
        np.array([1,0]),
        np.array([2,0]),
        np.array([2,1]),
        np.array([2,2]),
    ],

    # "pipe"
    [ 
        np.array([0,0]),
        np.array([0,1]),
        np.array([0,2]),
        np.array([0,3]),
    ],

    # "square"
    [ 
        np.array([0,0]),
        np.array([1,0]),
        np.array([0,1]),
        np.array([1,1]),
    ],
]

