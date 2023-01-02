#!/usr/bin/env python3

# adventOfCode 2022 day 24
# https://adventofcode.com/2022/day/24


import numpy as np

def get_input_state(input_filename):
    input_state = {
        'walls': list(),
        'blizards': list(),
        'entrance': None,
        'exit': None
    }
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_num, in_string in enumerate(f):
            in_list = list(in_string.rstrip())
            for col_num, ch in enumerate(in_list):
                if ch == '#':
                    input_state['walls'].append(np.array([col_num, line_num]))
            if line_num == 0:
                input_state['entrance'] = np.array([in_list.index('.'), line_num])
            else:
                if '.' in in_list:
                    input_state['exit'] = np.array([in_list.index('.'), line_num])
            print(in_string.rstrip())
    print()
    return input_state
    
def solve_problem(input_filename):
    state = get_input_state(input_filename)


solve_problem('input_sample0.txt')

