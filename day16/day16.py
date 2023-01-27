# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16


from dataclasses import dataclass
# from enum import Enum
# import copy

@dataclass
class Valve:
    name: str
    flow_rate: int
    valves_via_tunnel: list


# class ValveState(Enum):
#     IS_OPEN = 0
#     IS_CLOSED = 1

def create_valve(in_string):
    valve_constant = Valve(
        in_string[6:8], 
        int(in_string[in_string.index('=')+1:in_string.index(';')]),    
        in_string[9 + in_string.index('to valve'):].strip().split(', ')
    )
    return valve_constant


# def get_flow_rate(new_vsip, valve_constants):
#     '''
#     This returns total flow rate (combining all open valves' flow together)
#     '''
#     ret_val = 0
#     for label, v_s in new_vsip.items():
#         if v_s == ValveState.IS_OPEN:
#             ret_val += valve_constants[label].flow_rate
#     return ret_val


# def special_append(new_vsip, valve_states__in_process, min_total_loss):
#     # Do not keep considering new_vsip if it has run out of time
#     # The elapsed time is calculated from the length of the path, since
#     # all path steps (opening a valve, or following a single tunnel) take one minute
#     if len(new_vsip['PATH']) >= 31:
#         min_total_loss = min(min_total_loss, new_vsip['TOTAL_LOSS'])
#         return min_total_loss

#     # Do not keep considering new_vsip if it has a total loss that is greater
#     # or equal than the smallest that has already been shown to lead to all 
#     # valves being open
#     if new_vsip['TOTAL_LOSS'] > min_total_loss:
#         return min_total_loss

#     valve_states__in_process.append(new_vsip)
#     return min_total_loss


# def has_repeat(new_vsip, option):
#     '''
#     Note that a returned value of True says to abandon new_vsip
#     '''
#     for i in range(len(new_vsip['PATH']) - 1, -1, -1):
#         if new_vsip['PATH'][i] == 'OPENED':
#             # Found valve opening ... good
#             return False
            
#         if new_vsip['PATH'][i] == option:
#             # This is a repeat without any openings in between ... bad
#             return True
#     # If end reached ... good
#     return False

VALVE_CONSTANTS = dict()
NONZERO_VALVES = list()
SHORTEST_DISTANCE_BETWEEN_NONZERO_VALUES = dict()

# valve_states__in_process = [dict()]
# valve_states__finished = []

# # This is defined to be the flow rate when all valves are open
# max_flow_rate = 0

# # This is defined to be the smallest total loss seen
# min_total_loss = float('inf')

def already_visited(new_valve_dest):
    for the_value in valves_dest.values():
        if new_valve_dest in the_value:
            # break and continue with loop  ....   for new_valve_dest
            return True
    return False

# Reading input from the input file
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

del input_filename
del in_string
del f
del valve_constant


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


dummy = 123


#         max_flow_rate += int(in_string[23:].split(';')[0])
#         if valve_constants[valve_constant.name].flow_rate > 0:
#             valve_states__in_process[0][valve_constant.name] = ValveState.IS_CLOSED
#         else:
#             # Design decision: initially label valves with a flowrate of zero as "open"
#             # (The program logic will choose whether or not to open valves with 
#             # nonzero flowrate, and it will not bother wasting time on opening valves ]
#             # with a zero flow rate.  This is because the goal is to maximize the total
#             # pressure released in the first thirty minutes)
#             valve_states__in_process[0][valve_constant.name] = ValveState.IS_OPEN

# valve_states__in_process[0]['TOTAL_LOSS'] = 0
# valve_states__in_process[0]['PATH'] = ['AA']
# valve_states__in_process[0]['CURRENT_LOCATION'] = 'AA'

# while len(valve_states__in_process) > 0:
#     this_vsip = valve_states__in_process.pop()
#     current_location = this_vsip['CURRENT_LOCATION']



#     for option in valve_constants[current_location].valves_via_tunnel:
#         new_vsip = copy.deepcopy(this_vsip)
#         new_vsip['CURRENT_LOCATION'] = option
#         curr_flow_loss = max_flow_rate - get_flow_rate(new_vsip, valve_constants)
#         new_vsip['TOTAL_LOSS'] += curr_flow_loss

#         # Do not keep considering new_vsip if this is a repeat visit to that valve and there haven't been any valve openings since then
#         if has_repeat(new_vsip, option):
#             continue

#         new_vsip['PATH'].append(option)
#         min_total_loss = special_append(new_vsip, valve_states__in_process, min_total_loss)

#     if this_vsip[current_location] == ValveState.IS_CLOSED:
#         new_vsip = copy.deepcopy(this_vsip)
#         new_vsip['TOTAL_LOSS'] += curr_flow_loss
#         new_vsip['PATH'].append('OPENED')
#         curr_flow_loss = max_flow_rate - get_flow_rate(new_vsip, valve_constants)
#         new_vsip[current_location] = ValveState.IS_OPEN
        
#         # conditional on whether at least one valve (with a flowrate) remains closed
#         if curr_flow_loss > 0:
#             # inside function -- conditional on whether out of time ... based on len(new_vsip['PATH'])
#             special_append(new_vsip, valve_states__in_process, min_total_loss)
#         else:
#             min_total_loss = min(min_total_loss, new_vsip['TOTAL_LOSS'])


# print(f'The "total loss" is : {min_total_loss}')
# print(f'The answer to part A is {30 * max_flow_rate - min_total_loss}')



