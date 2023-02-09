# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16


from dataclasses import dataclass
from itertools import permutations
import copy
import itertools

@dataclass
class Valve:
    name: str
    flow_rate: int
    valves_via_tunnel: list


def create_valve(in_string):
    valve_constant = Valve(
        in_string[6:8], 
        int(in_string[in_string.index('=')+1:in_string.index(';')]),    
        in_string[9 + in_string.index('to valve'):].strip().split(', ')
    )
    return valve_constant


def get_pressure_released(open_valves):
    ret_val = 0
    for valve_id, timestamp_on in open_valves.items():
        ret_val += VALVE_CONSTANTS[valve_id].flow_rate * (TIME_LIMIT - timestamp_on)
    return ret_val


def add_valve(remaining_valves: list, open_valves: dict, player_locations: set, current_valve: str):
    ret_val = 0
    start_time = open_valves[current_valve]

    for j, next_valve in enumerate(remaining_valves):
        end_time = start_time + SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[current_valve][next_valve] + 1

        remaining_valves_av = copy.deepcopy(remaining_valves)
        remaining_valves_av.pop(j)

        open_valves_av = copy.deepcopy(open_valves)
        open_valves_av[next_valve] = end_time

        player_locations_av = copy.deepcopy(player_locations)
        player_locations_av.remove(current_valve)
        player_locations_av.add(next_valve)

        if end_time == TIME_LIMIT:
            ret_val = max(ret_val, get_pressure_released(open_valves_av))
        if end_time > TIME_LIMIT:
            open_valves_av.pop(next_valve)
            ret_val = max(ret_val, get_pressure_released(open_valves_av))
        else:
            if len(remaining_valves_av) == 0:
                ret_val = max(ret_val, get_pressure_released(open_valves_av))
            else:

                # Determine which player location is next to explore branches in
                best_timestamp = float('inf')
                next_valves = []
                for player_valve in player_locations_av:
                    if player_valve not in open_valves_av:
                        continue
                    player_timestamp = open_valves_av[player_valve]
                    if  player_timestamp == best_timestamp:
                        next_valves.append(player_valve)
                    if  player_timestamp < best_timestamp:
                        next_valves = [player_valve]
                    for next_valve in next_valves:
                        ret_val = max(ret_val, add_valve(remaining_valves_av, open_valves_av, player_locations_av, next_valve))

    return ret_val


def already_visited(new_valve_dest, valves_dest):
    for the_value in valves_dest.values():
        if new_valve_dest in the_value:
            # Determined that it's been already visited
            return True
    # Hasn't been already visited
    return False

# Read input from the input file
# Fill in valve_constants and nonzero_valves
def get_input(input_filename):
    valve_constants = dict()
    nonzero_valves = list()
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)

            valve_constant = create_valve(in_string)
            valve_constants[valve_constant.name] = valve_constant
            if valve_constant.flow_rate > 0:
                nonzero_valves.append(valve_constant.name)
        print()
    return valve_constants, nonzero_valves


# Use VALVE_CONSTANTS and NONZERO_VALVES to develop a graph describing distances 
# between all non-zero flowrate valves
def get_sdbnv(VALVE_CONSTANTS, NONZERO_VALVES):
    for valve_orig in NONZERO_VALVES:
        SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig] = {valve_orig: 0}
        valves_dest = {0:[valve_orig]}
        while len(SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig]) < len(NONZERO_VALVES):
            old_distance = min(valves_dest.keys())
            valve_old_dest = valves_dest[old_distance].pop()
            if len(valves_dest[old_distance]) == 0:
                del valves_dest[old_distance]
            for new_valve_dest in VALVE_CONSTANTS[valve_old_dest].valves_via_tunnel:
                if already_visited(new_valve_dest, valves_dest):
                    continue
                if old_distance + 1 not in valves_dest:
                    valves_dest[old_distance + 1] = []
                valves_dest[old_distance + 1].append(new_valve_dest)
                if VALVE_CONSTANTS[new_valve_dest].flow_rate > 0:
                    SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig][new_valve_dest] = old_distance + 1
            if float('inf') not in valves_dest:
                valves_dest[float('inf')] = list()
            valves_dest[float('inf')].append(valve_old_dest)
    return SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES


# If starting state was at a valve with a flowrate > 0, then SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES would have all that's needed to solve the problem.  However, both given examples have the starting position at a zero flowrate valve.
def get_initial_nonzero_valves(NONZERO_VALVES, VALVE_CONSTANTS):
    known_valves = dict()
    curr_valves = {INITIAL_POSITION_OF_ALL_PLAYERS: 0}
    

    # next_valves = list()
    while len(curr_valves) > 0:
        curr_valve, path_distance = curr_valves.popitem()
        if curr_valve in known_valves:
            continue
        if curr_valve in NONZERO_VALVES:
            known_valves[curr_valve] = path_distance + 1
            continue
        else:
            known_valves[curr_valve] = None
        for next_valve in VALVE_CONSTANTS[curr_valve].valves_via_tunnel:
            if next_valve not in known_valves:
                curr_valves[next_valve] = path_distance + 1
    valves_to_pop = list()
    for valve_id, distance in known_valves.items():
        if distance is None:
            valves_to_pop.append(valve_id)
    for valve_id in valves_to_pop:
        known_valves.pop(valve_id)
    return known_valves

START_TIME = 0

INITIAL_POSITION_OF_ALL_PLAYERS = 'AA'
TIME_LIMIT = 26
NUMBER_OF_PLAYERS = 2 if TIME_LIMIT == 26 else 1
player_locations = set()

SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES = dict()

# Input filename is on the next line .... (so I can find it easily ! )

VALVE_CONSTANTS, NONZERO_VALVES = get_input('input_sample0.txt')

SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES = get_sdbnv(VALVE_CONSTANTS, NONZERO_VALVES)
INITIAL_NONZERO_VALVES = get_initial_nonzero_valves(NONZERO_VALVES, VALVE_CONSTANTS)
max_pressure_released = 0
ret_val = 0


for init_valves__tuples_nested in itertools.permutations(INITIAL_NONZERO_VALVES.items(), NUMBER_OF_PLAYERS):
    remaining_valves = copy.deepcopy(NONZERO_VALVES)
    open_valves = dict()
    end_time = float('inf')
    for k,v in init_valves__tuples_nested:
        open_valves[k] = v
        remaining_valves.remove(k)
        player_locations.add(k)


    # Given the player locations for this particular one of the itertools.permutations (above), list the valves with the earliest arrival timestamp

    next_valves = [
        valve
        for valve in open_valves.keys()
        if open_valves[valve] == min(open_valves.values())
    ]

    # recursive calls
    for next_valve in next_valves:
        ret_val = max(ret_val, add_valve(remaining_valves, open_valves, player_locations, next_valve))

print(f'The maximum pressure that can be released is: {ret_val}\n')




