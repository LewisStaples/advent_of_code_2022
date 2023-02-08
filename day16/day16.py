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

    # # path_dict is {'valve_path': list_of_valves, 'path_durations': list_of_durations}
    # curr_total_flow_rate = 0
    # duration_total = 0
    # pressure_released = 0

    # for valve_index in range(len(path_dict['valve_path'])):
    #     duration_this_valve = path_dict['path_durations'][valve_index]
    #     duration_total += duration_this_valve
    #     pressure_released += duration_this_valve * curr_total_flow_rate
    #     curr_total_flow_rate += VALVE_CONSTANTS[path_dict['valve_path'][valve_index]].flow_rate
        
    # if duration_total < TIME_LIMIT:
    #     pressure_released += (TIME_LIMIT - duration_total) * curr_total_flow_rate

    # return pressure_released


# def add_valve(remaining_valves_av, open_valves_av, player_locations):
# def add_valve(remaining_valves, open_valves, player_locations): # , next_valve):

# def add_valve(remaining_valves, open_valves, player_locations, newest_valve):
def add_valve(remaining_valves, open_valves, current_valve):
#     # next_valve = next_valves_av.pop()
    ret_val = 0
    start_time = open_valves[current_valve]
    current_valve_av = copy.deepcopy(current_valve)

    # start_time = open_valves[newest_valves[0]]
    
#     for i, newest_valve in enumerate(newest_valves):
#         newest_valves_av = copy.deepcopy(newest_valves)
#         newest_valve_av = newest_valves_av.pop(i)

#     # newest_valves_av = [
#     #     valve
#     #     for valve in open_valves.keys()
#     #     if open_valves[valve] == min(open_valves.values())
#     # ]

    for j, next_valve in enumerate(remaining_valves):
        end_time = start_time + SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[current_valve_av][next_valve] + 1

        remaining_valves_av = copy.deepcopy(remaining_valves)
        remaining_valves_av.pop(j)

        open_valves_av = copy.deepcopy(open_valves)
        open_valves_av[next_valve] = end_time

#             # newest_valves_av = [
#             #     valve
#             #     for valve in open_valves.keys()
#             #     if open_valves[valve] == min(open_valves.values())
#             # ]


        if end_time == TIME_LIMIT:
            ret_val = max(ret_val, get_pressure_released(open_valves_av))
        if end_time > TIME_LIMIT:
            open_valves_av.pop(next_valve)
            ret_val = max(ret_val, get_pressure_released(open_valves_av))
        else:
            if len(remaining_valves_av) == 0:
                ret_val = max(ret_val, get_pressure_released(open_valves_av))
            else:
                # ret_val = max(ret_val, add_valve(remaining_valves_av, open_valves_av, player_locations, newest_valve_av))
                ret_val = max(ret_val, add_valve(remaining_valves_av, open_valves_av, next_valve))

# # add_valve(remaining_valves, open_valves, player_locations, newest_valves)

    return ret_val




#             # If it's hit the time limit, get_pressure_released
#             # If it's over the time limit, remove the latest added valve and get_pressure_released
#             # If it's under the time limit
#                 # If no valves remaining, get_pressure_released
#                 # Otherwise, do recursive call to add another valve

#     # if len(remaining_valves_sf) == 0:
#     #     ret_val = max(ret_val, get_pressure_released(path))
#     # elif sum(path['path_durations']) == TIME_LIMIT:
#     #     ret_val = max(ret_val, get_pressure_released(path))
#     # elif sum(path['path_durations']) < TIME_LIMIT:
#     #     for i_new in range(len(remaining_valves_sf)):
#     #         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves_sf), copy.deepcopy(path), i_new))
#     # else:




# # This function uses recursion to add a valve.
# # Then it calculates elapsed time versus the time limit, 
# # as well as if all valves have been opened.
# #
# # On the basis of those results it may attempt to 
# # add new valves (with a recursive call to itself), 
# # or stop adding valves, in which case it calls 
# # get_pressure_released to get the pressure released
# # from this sequence of valves

# # def add_valve(remaining_valves_sf, path, i):
#     # ret_val = 0
#     # next_valve = remaining_valves_sf.pop(i)
#     # path['path_durations'].append(SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES[path['valve_path'][-1]][next_valve] + 1)
#     # path['valve_path'].append(next_valve)
#     # if len(remaining_valves_sf) == 0:
#     #     ret_val = max(ret_val, get_pressure_released(path))
#     # elif sum(path['path_durations']) == TIME_LIMIT:
#     #     ret_val = max(ret_val, get_pressure_released(path))
#     # elif sum(path['path_durations']) < TIME_LIMIT:
#     #     for i_new in range(len(remaining_valves_sf)):
#     #         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves_sf), copy.deepcopy(path), i_new))
#     # else:
#     #     # Addition of the most recent valve exceeded the time limit,
#     #     # therefore remove that most recent valve, so you won't
#     #     # calculate total pressure released for a forbidden combinations of open valves
#     #     path['path_durations'].pop()
#     #     path['valve_path'].pop()

#     #     p_release = get_pressure_released(path)
#     #     ret_val = max(ret_val, p_release)
#     #     
#     # return ret_val


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
    return known_valves

START_TIME = 0


TIME_LIMIT = 30
NUMBER_OF_PLAYERS = 2 if TIME_LIMIT == 26 else 1
# player_locations = list()

SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES = dict()
VALVE_CONSTANTS, NONZERO_VALVES = get_input('input_sample0.txt')
SHORTEST_DISTANCE_BETWEEN_NONZERO_VALVES = get_sdbnv(VALVE_CONSTANTS, NONZERO_VALVES)
INITIAL_NONZERO_VALVES = get_initial_nonzero_valves(NONZERO_VALVES, VALVE_CONSTANTS)
max_pressure_released = 0
ret_val = 0


# LOGIC WITH OLD DATA STRUCTURES ...
# for init_valve, init_duration in INITIAL_NONZERO_VALVES.items():
#     remaining_valves = copy.deepcopy(NONZERO_VALVES)
#     remaining_valves.remove(init_valve)

#     path_dict = {'valve_path': [init_valve], 'path_durations': [init_duration]}
    
#     for i in range(len(remaining_valves)):
#         # recursive call
#         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves), copy.deepcopy(path_dict), i))

# print(f'Maximum pressure released of all paths is: {ret_val}\n')



# for init_valve, v1_end_time in INITIAL_NONZERO_VALVES.items():
for init_valves__tuples_nested in itertools.permutations(INITIAL_NONZERO_VALVES.items(), NUMBER_OF_PLAYERS):
    remaining_valves = copy.deepcopy(NONZERO_VALVES)
    open_valves = dict()
    end_time = float('inf')
    for k,v in init_valves__tuples_nested:
        open_valves[k] = v
        remaining_valves.remove(k)
        # player_locations.append(k)
    
    next_valves = [
        valve
        for valve in open_valves.keys()
        if open_valves[valve] == min(open_valves.values())
    ]

    # recursive calls
    for next_valve in next_valves:
        # ret_val = max(ret_val, add_valve(remaining_valves, open_valves, player_locations, next_valve))
        ret_val = max(ret_val, add_valve(remaining_valves, open_valves, next_valve))

print(f'Final answer: {ret_val}')


#         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves), copy.deepcopy(path_dict), i))





#     # for i in range(len(remaining_valves)):
#     for valves_next in itertools.permutations(remaining_valves,  NUMBER_OF_PLAYERS):
#         player_locations = list(valves_next)
#         # recursive call
#         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves), copy.deepcopy(open_valves), player_locations))
# #         ret_val = max(ret_val, add_valve(copy.deepcopy(remaining_valves), copy.deepcopy(path_dict), i))


