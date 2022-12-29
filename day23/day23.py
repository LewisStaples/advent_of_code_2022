# adventOfCode 2022 day 23
# https://adventofcode.com/2022/day/23


import numpy as np

def get_input(input_filename):
    elf_map = set()

    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for y, in_string in enumerate(f):
            in_string = in_string.rstrip()
            for x, ch in enumerate(in_string):
                if ch == '#':
                    elf_map.add((x,y))
    return elf_map

def display_elf_map(elf_map, map_title):
    print(map_title)
    margins = {'top': float('inf'), 'right': float('-inf'), 'bottom': float('-inf'), 'left': float('inf')}
    for point in elf_map:
        margins['top'] = min(margins['top'], point[1])
        margins['right'] = max(margins['right'], point[0])
        margins['bottom'] = max(margins['bottom'], point[1])
        margins['left'] = min(margins['left'], point[0])
    for y in range(margins['top'], margins['bottom'] + 1):
        for x in range(margins['left'], margins['right'] + 1):
            if (x,y) in elf_map:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def get_proposed_moves(elf_map, round_number):
    eight_compass_points = [
        np.array([1,1]),
        np.array([1,0]),
        np.array([1,-1]),
        np.array([0,1]),
        np.array([0,-1]),
        np.array([-1,1]),
        np.array([-1,0]),
        np.array([-1,-1])
    ]
    proposed_moves = dict()
    for elf_location in elf_map:
        # Determine if this elf has at least one adjacent elf
        any_adjacents = False
        elf_location = np.array(elf_location)
        for direction in eight_compass_points:
            adjacent_location = tuple(elf_location + direction)
            if adjacent_location in elf_map:
                any_adjacents = True
                break
        if not any_adjacents:
            break
        
        # See which direction the elf proposes to move in

        # Check if that proposed destination is already in proposed_moves
        # If yes, mark that proposed_move as unreachable





def do_rounds(elf_map):
    for round_number in range(1, 3):
        # pad_edges(elf_map)
        get_proposed_moves(elf_map, round_number)
        display_elf_map(elf_map, f'Elf map after round {round_number}')



def solve_problem(input_filename):
    elf_map = get_input(input_filename)
    display_elf_map(elf_map, 'Initial elf map')
    do_rounds(elf_map)


solve_problem('input_scenario0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')
    
