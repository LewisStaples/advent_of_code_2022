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

def get_margins(elf_map):
    margins = {'top': float('inf'), 'right': float('-inf'), 'bottom': float('-inf'), 'left': float('inf')}
    for point in elf_map:
        margins['top'] = min(margins['top'], point[1])
        margins['right'] = max(margins['right'], point[0])
        margins['bottom'] = max(margins['bottom'], point[1])
        margins['left'] = min(margins['left'], point[0])
    return margins


def display_elf_map(elf_map, map_title):
    print(map_title)
    margins = get_margins(elf_map)
    for y in range(margins['top'], margins['bottom'] + 1):
        for x in range(margins['left'], margins['right'] + 1):
            if (x,y) in elf_map:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def required_vacancies_not_present(required_vacancies, elf_map):
    for vacancy in required_vacancies:
        if vacancy in elf_map:
            # Found one instance where the requirement is not met
            # One elf has been found to be present where a vacancy is required
            # (Note that there might be others, too)
            return True
    # The requirements are met: the required vacancies are all vacant
    return False


def make_moves(elf_map, round_number):
    eight_compass_points = [
        np.array([1,0]),  # Right / East
        np.array([1,1]),  # SE
        np.array([0,1]),  # Down / South
        np.array([-1,1]), # SW
        np.array([-1,0]), # Left / West
        np.array([-1,-1]), # NW
        np.array([0,-1]), # Up / North
        np.array([1,-1]), # NE
    ]
    proposal_matrix = {
        1:  {
            'proposed_direction': eight_compass_points[6],
            'required_vacancies': [
                eight_compass_points[5],
                eight_compass_points[6],
                eight_compass_points[7],
                ]
            },
        2:  {
            'proposed_direction': eight_compass_points[2],
            'required_vacancies': [
                eight_compass_points[1],
                eight_compass_points[2],
                eight_compass_points[3],
                ]
            },
        3:  {
            'proposed_direction': eight_compass_points[4],
            'required_vacancies': [
                eight_compass_points[3],
                eight_compass_points[4],
                eight_compass_points[5],
                ]
            },
        0:  {
            'proposed_direction': eight_compass_points[0],
            'required_vacancies': [
                eight_compass_points[7],
                eight_compass_points[0],
                eight_compass_points[1],
                ]
            },
    }
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
            continue
        
        # See which direction the elf proposes to move in
        first_proposal_index = round_number % 4
        for i in range(4):
            proposal_index = (first_proposal_index + i) % 4
            proposal_fields = proposal_matrix[proposal_index]

            proposed_destination = tuple(elf_location + proposal_fields['proposed_direction'])
            required_vacancies = [tuple(elf_location + x) for x in proposal_fields['required_vacancies']]
            if required_vacancies_not_present(required_vacancies, elf_map):
                continue
            else:
                # Check if that proposed destination is already in proposed_moves
                if proposed_destination in proposed_moves:
                    # If it's already there, mark that proposed_move as unreachable with a None (it's a flag)
                    proposed_moves[proposed_destination] = None
                else:
                    # This proposed_destination hasn't been seen before, so list it as a proposed_move
                    proposed_moves[proposed_destination] = tuple(elf_location)
                break

    # Disregarding any moves where more than one elf intends to move to there
    proposed_moves_pruned = {k: v for k, v in proposed_moves.items() if v is not None}

    elf_map -= set(proposed_moves_pruned.values())
    elf_map.update(proposed_moves_pruned.keys())

def get_empty_tile_count(elf_map):
    margins = get_margins(elf_map)
    total_tile_count = ( margins['bottom'] - margins['top'] + 1) * ( margins['right'] - margins['left'] + 1 )
    empty_tile_count = total_tile_count - len(elf_map)
    return empty_tile_count

def do_rounds(elf_map):
    for round_number in range(1, 11):
        make_moves(elf_map, round_number)
        # display_elf_map(elf_map, f'Elf map after round {round_number}')

    empty_tile_count = get_empty_tile_count(elf_map)
    print(f'The answer to part A is {empty_tile_count}\n')





def solve_problem(input_filename):
    elf_map = get_input(input_filename)
    do_rounds(elf_map)


solve_problem('input_sample1.txt')


    