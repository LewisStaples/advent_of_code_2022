# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16


from dataclasses import dataclass
from itertools import permutations
import copy

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


def get_pressure_released(path_dict):
    # path_dict is {'valve_path': list_of_valves, 'path_durations': list_of_durations}
    curr_total_flow_rate = 0
    duration_total = 0
    pressure_released = 0

    for valve_index in range(len(path_dict['valve_path'])):
        duration_this_valve = path_dict['path_durations'][valve_index]
        duration_total += duration_this_valve
        pressure_released += duration_this_valve * curr_total_flow_rate
        curr_total_flow_rate += VALVE_CONSTANTS[path_dict['valve_path'][valve_index]].flow_rate
        
    if duration_total < TIME_LIMIT:
        pressure_released += (TIME_LIMIT - duration_total) * curr_total_flow_rate

    # print(pressure_released)
    return pressure_released, curr_total_flow_rate


def special_function(remaining_valves_sf, path, i):
    ret_val = 0
    next_valve = remaining_valves_sf.pop(i)
    path['path_durations'].append(SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[path['valve_path'][-1]][next_valve] + 1)
    path['valve_path'].append(next_valve)
    if len(remaining_valves_sf) == 0:
        ret_val = max(ret_val, get_pressure_released(path)[0])
    elif sum(path['path_durations']) == TIME_LIMIT:
        ret_val = max(ret_val, get_pressure_released(path)[0])
    elif sum(path['path_durations']) < TIME_LIMIT:
        for i_new in range(len(remaining_valves_sf)):
            ret_val = max(ret_val, special_function(copy.deepcopy(remaining_valves_sf), copy.deepcopy(path), i_new))

            dummy = 123

    else:
        path['path_durations'].pop()
        path['valve_path'].pop()

        p_release, ending_flowrate = get_pressure_released(path)
        ret_val = max(ret_val, p_release)
    return ret_val


TIME_LIMIT = 30

VALVE_CONSTANTS = dict()
NONZERO_VALVES = list()
SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES = dict()

def already_visited(new_valve_dest):
    for the_value in valves_dest.values():
        if new_valve_dest in the_value:
            # Determined that it's been already visited
            return True
    # Hasn't been already visited
    return False

FULL_BLAST_FLOWRATE = 0
# Read input from the input file
# Fill in VALVE_CONSTANTS and NONZERO_VALVES
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

        valve_constant = create_valve(in_string)
        VALVE_CONSTANTS[valve_constant.name] = valve_constant
        if valve_constant.flow_rate > 0:
            NONZERO_VALVES.append(valve_constant.name)
        
        FULL_BLAST_FLOWRATE += valve_constant.flow_rate
    print()
del input_filename
del in_string
del f
del valve_constant

# Use VALVE_CONSTANTS and NONZERO_VALVES to develop a graph describing distances 
# between all non-zero flowrate valves
for valve_orig in NONZERO_VALVES:
    SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig] = {valve_orig: 0}
    valves_dest = {0:[valve_orig]}
    while len(SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig]) < len(NONZERO_VALVES):
        old_distance = min(valves_dest.keys())
        valve_old_dest = valves_dest[old_distance].pop()
        if len(valves_dest[old_distance]) == 0:
            del valves_dest[old_distance]
        for new_valve_dest in VALVE_CONSTANTS[valve_old_dest].valves_via_tunnel:
            if already_visited(new_valve_dest):
                continue
            if old_distance + 1 not in valves_dest:
                valves_dest[old_distance + 1] = []
            valves_dest[old_distance + 1].append(new_valve_dest)
            if VALVE_CONSTANTS[new_valve_dest].flow_rate > 0:
                SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[valve_orig][new_valve_dest] = old_distance + 1
        if float('inf') not in valves_dest:
            valves_dest[float('inf')] = list()
        valves_dest[float('inf')].append(valve_old_dest)

del valve_orig
del valve_old_dest
del old_distance
del new_valve_dest
del valves_dest


# If starting state was at a valve with a flowrate > 0, then SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES would have all that's needed to solve the problem.  However, both given examples have the starting position at a zero flowrate valve.

known_valves = dict()
curr_valves = {'AA': 0}
next_valves = list()
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
INITIAL_NONZERO_VALVES = known_valves
del known_valves
del valve_id
del path_distance
del next_valves
del next_valve
del distance
del valves_to_pop
del curr_valves
del curr_valve

# TESTING ONLY !!!!!!
# path['valve_path'] = ['DD', 'JJ', 'CC', 'HH', 'BB', 'EE']
# path['path_durations'] = [2, 4, 5, 6, 7, 4]

# path_dict = {'valve_path': ['DD', 'BB'], 'path_durations': [2, 3]}
path_dict = {'valve_path': ['KM', 'IC', 'GB', 'OE', 'KT', 'AK'], 'path_durations': [3, 4, 4, 10, 3, 3]}
# get_pressure_released(path_dict)

max_pressure_released = 0
ret_val = 0
for init_valve, init_duration in INITIAL_NONZERO_VALVES.items():
    remaining_valves = copy.deepcopy(NONZERO_VALVES)
    remaining_valves.remove(init_valve)

    path_dict = {'valve_path': [init_valve], 'path_durations': [init_duration]}
    
    for i in range(len(remaining_valves)):
        # recursive call
        ret_val = max(ret_val, special_function(copy.deepcopy(remaining_valves), copy.deepcopy(path_dict), i))

print(f'Maximum pressure released of all paths is: {ret_val}\n')

