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


def get_pressure_released(valve, duration, extra_valves):


    # print(f'Inputs: {duration}: {valve}, {extra_valves}')


    curr_total_flow_rate = VALVE_CONSTANTS[valve].flow_rate
    duration += 1
    # ret_val = curr_total_flow_rate
    ret_val = 0


    
    while True:
        if len(extra_valves) == 0:
            ret_val += curr_total_flow_rate * (30 - duration)
            break
        next_valve = extra_valves.pop(0)
        time_interval = SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES[valve][next_valve] + 1
        duration += time_interval
        if duration + time_interval >= 30:
            ret_val += curr_total_flow_rate * (30 - duration)
            break
        ret_val += time_interval * curr_total_flow_rate
        # if len(extra_valves) == 0:
        #     break
        # ret_val = duration * curr_total_flow_rate
        valve = next_valve
        curr_total_flow_rate += VALVE_CONSTANTS[valve].flow_rate
    # print(ret_val)
    return ret_val


VALVE_CONSTANTS = dict()
NONZERO_VALVES = list()
SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES = dict()

def already_visited(new_valve_dest):
    for the_value in valves_dest.values():
        if new_valve_dest in the_value:
            # Determined that it's been already visited
            return True
    # Hasn't been already visited
    return False

# Read input from the input file
# Fill in VALVE_CONSTANTS and NONZERO_VALVES
input_filename='input_sample0.txt'
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
    print()
del input_filename
del in_string
del f
del valve_constant

# Use VALVE_CONSTANTS and NONZERO_VALVES to develop a graph describing distances 
# between all non-zero flowrate valves
for valve_orig in NONZERO_VALVES:
    SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES[valve_orig] = {valve_orig: 0}
    valves_dest = {0:[valve_orig]}
    while len(SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES[valve_orig]) < len(NONZERO_VALVES):
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
                SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES[valve_orig][new_valve_dest] = old_distance + 1
        if float('inf') not in valves_dest:
            valves_dest[float('inf')] = list()
        valves_dest[float('inf')].append(valve_old_dest)

del valve_orig
del valve_old_dest
del old_distance
del new_valve_dest
del valves_dest


# If starting state was at a valve with a flowrate > 0, then SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES would have all that's needed to solve the problem.  However, both given examples have the starting position at a zero flowrate valve.

known_valves = dict()
curr_valves = {'AA': 0}
next_valves = list()
while len(curr_valves) > 0:
    curr_valve, path_distance = curr_valves.popitem()
    if curr_valve in known_valves:
        continue
    if curr_valve in NONZERO_VALVES:
        known_valves[curr_valve] = path_distance
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

# # TESTING ONLY !!!!!!
# get_pressure_released('DD', 1, ['BB', 'JJ', 'HH', 'EE', 'CC'])




max_pressure_released = 0
for init_valve, init_duration in INITIAL_NONZERO_VALVES.items():
    remaining_valves = copy.copy(NONZERO_VALVES)
    remaining_valves.remove(init_valve)
    for extra_valves in permutations(remaining_valves, len(remaining_valves)):
        max_pressure_released = max(max_pressure_released, get_pressure_released(init_valve, init_duration, list(extra_valves)))

print(f'Maximum pressure released of all paths is: {max_pressure_released}\n')

