#!/usr/bin/env python3

# adventOfCode 2022 day 24
# https://adventofcode.com/2022/day/24


import numpy as np

direction = {
    '^': {'vector': (0,-1), 'opposite_distance': None},
    'v': {'vector': (0,1), 'opposite_distance': None},
    '<': {'vector': (-1,0), 'opposite_distance': None},
    '>': {'vector': (1,0), 'opposite_distance': None}
}

def get_initial_state(input_filename):
    initial_state = {
        'walls': set(),
        'blizzards_locations': list(),
        'blizzards_directions': list(),
        # 'blizzards': dict(),
        'entrance': None,
        'exit': None
    }
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    print('Displaying original input:')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_num, in_string in enumerate(f):
            in_list = list(in_string.rstrip())
            for col_num, ch in enumerate(in_list):
                if ch == '#':
                    initial_state['walls'].add((col_num, line_num))
                if ch in direction:
                    # initial_state['blizzards'][(col_num, line_num)] = ch # direction[ch]['vector']
                    # initial_state['blizzards_locations'].add((col_num, line_num))
                    # initial_state['blizzards_directions'].add(direction[ch]['vector'])

                    initial_state['blizzards_locations'].append(np.array([col_num, line_num]))
                    initial_state['blizzards_directions'].append(direction[ch])
            if line_num == 0:
                initial_state['entrance'] = (in_list.index('.'), line_num)
                # The below line prevents the expedition from exiting the valley via the entrance site
                initial_state['walls'].add((in_list.index('.'), -1))
            print(in_string.rstrip())
    print()
    initial_state['exit'] = (in_list.index('.'), line_num)
    initial_state['minute_counter'] = 0
    initial_state['keep_going'] = True
    initial_state['poss_curr_expedition_locns'] = {initial_state['entrance']}
    initial_state['valley_dimensions'] = (len(in_list), line_num + 1)

    direction['^']['opposite_distance'] = (0, line_num - 1)
    direction['v']['opposite_distance'] = (0, 1 - line_num)
    direction['<']['opposite_distance'] = (len(in_list) - 2, 0)
    direction['>']['opposite_distance'] = (2 - len(in_list), 0)
    return initial_state


def advance_one_minute(state):
    state['minute_counter'] += 1

    # Update blizzard state
    for the_index in range(len(state['blizzards_locations'])):
        # advance all blizzards by one unit
        state['blizzards_locations'][the_index] += state['blizzards_directions'][the_index]['vector']
        if tuple(state['blizzards_locations'][the_index]) in state['walls']:
            state['blizzards_locations'][the_index] += state['blizzards_directions'][the_index]['opposite_distance']

    # update expedition list of possible states
    new_poss_curr_expedition_locns = set()
    for curr_locn in state['poss_curr_expedition_locns']:
        new_pot_locns = {curr_locn}
        for dir_grp in direction.values():
            # new_locn = curr_locn + dir_grp['vector']
            new_locn = (
                curr_locn[0] + dir_grp['vector'][0],
                curr_locn[1] + dir_grp['vector'][1],
            )
            # Don't repeat any new_pot_locns
            # if any((new_locn == x).all() for x in new_pot_locns):
            if new_locn in new_pot_locns:
                break
            new_pot_locns.add(new_locn)
        for new_pot_locn in new_pot_locns:
            # If this location has already been identified as a good one, skip it
            # if any((new_pot_locn == x).all() for x in new_poss_curr_expedition_locns):
            # if list(new_pot_locn) in [list(x) for x in new_poss_curr_expedition_locns]:
            if new_pot_locn in new_poss_curr_expedition_locns:
                continue

            # If it's a wall, skip it
            # if any((new_pot_locn == x).all() for x in state['walls']):
            # if list(new_pot_locn) in [list(x) for x in state['walls']]:
            if new_pot_locn in state['walls']:
                continue

            # If exit ... finished
            # if np.array_equal(new_pot_locn, state['exit']):
            if new_pot_locn == state['exit']:
                return state['minute_counter']

            # # If blizzard, skip it
            if any((np.array(list(new_pot_locn)) == x).all() for x in state['blizzards_locations']):
            # if list(new_pot_locn) in [list(x) for x in state['blizzards_locations']]:
                continue

            # It's a good location, so add it to the list of new locations
            new_poss_curr_expedition_locns.add(new_pot_locn)

    state['poss_curr_expedition_locns'] = new_poss_curr_expedition_locns

    # Not finished
    return None


def display(state):
    # if len(state['walls']) > 50:
    #     return

    # Display timestamp
    print(f"Valley at minute {state['minute_counter']}")

    if len(state['walls']) > 50:
        return

    # Loop through coordinates
    for j in range(state['valley_dimensions'][1]):
        for i in range(state['valley_dimensions'][0]):
            # Display wall
            if any((np.array([i,j]) == x).all() for x in state['walls']):
                print('#', end='')
                continue

            # Display blizzard ('B' will be shown for all blizzards, regardless of their direction)
            if any((np.array([i,j]) == x).all() for x in state['blizzards_locations']):
                print('B', end='')
                continue

            # Expedition location will not be displayed

            # Display entrance
            if np.array_equal(np.array([i,j]), state['entrance']):
                print('N', end='')
                continue

            # Display exit
            if np.array_equal(np.array([i,j]), state['exit']):
                print('X', end='')
                continue

            # Display empty space
            print('.', end='')
        print()
    print()

def get_minutes_to_goal(state):
    # display(state)

    while state['keep_going']:
        aom = advance_one_minute(state)
        if aom is not None:
            return aom

        display(state)



def solve_problem(input_filename):
    state = get_initial_state(input_filename)
    minutes_to_goal = get_minutes_to_goal(state)
    print(f'The answer to part A is {minutes_to_goal}\n')

solve_problem('input.txt')

