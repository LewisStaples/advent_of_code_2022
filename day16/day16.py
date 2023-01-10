# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16


from dataclasses import dataclass
from enum import Enum
import copy

@dataclass
class Valve:
    name: str
    flow_rate: int
    valves_via_tunnel: list


class ValveState(Enum):
    IS_OPEN = 0
    IS_CLOSED = 1

def create_valve(in_string):
    valve_constant = Valve(
        in_string[6:8], 
        int(in_string[in_string.index('=')+1:in_string.index(';')]),    
        in_string[9 + in_string.index('to valve'):].strip().split(', ')
    )
    return valve_constant

# TESTING ONLY !!!!!!!!
def see_if_match(this_vsip):
    path = this_vsip['PATH']
    if len(path) < 25:
        return

    if path[1] != 'DD':
        return
    if path[2] != 'OPENED':
        return
    

    
    if path[3] != 'CC':
        return

    if path[4] != 'BB':
        return

    if path[5] != 'OPENED':
        return

    if path[6] != 'AA':
        return

    if path[7] != 'II':
        return

    if path[8] != 'JJ':
        return

    if path[9] != 'OPENED':
        return

    if path[10] != 'II':
        return

    if path[11] != 'AA':
        return

    if path[12] != 'DD':
        return

    if path[13] != 'EE':
        return

    if path[14] != 'FF':
        return

    if path[15] != 'GG':
        return

    if path[16] != 'HH':
        return

    if path[17] != 'OPENED':
        return

    if path[18] != 'GG':
        return

    if path[19] != 'FF':
        return

    if path[20] != 'EE':
        return

    if path[21] != 'OPENED':
        return

    if path[22] != 'DD':
        return

    if path[23] != 'CC':
        return

    if path[24] != 'OPENED':
        return

    dummy = 123
    
    print()
    print(f'SUCCESS ... State is:')
    print(this_vsip)
    print()
    print()



def get_flow_rate(new_vsip, valve_constants):
    '''
    This returns total flow rate (combining all open valves' flow together)
    '''
    ret_val = 0
    for label, v_s in new_vsip.items():
        if v_s == ValveState.IS_OPEN:
            ret_val += valve_constants[label].flow_rate
    return ret_val


def special_append(new_vsip, valve_states__in_process, min_total_loss):
    # Do not keep considering new_vsip if it has run out of time
    # The elapsed time is calculated from the length of the path, since
    # all path steps (opening a valve, or following a single tunnel) take one minute
    if len(new_vsip['PATH']) >= 31:
        min_total_loss = min(min_total_loss, new_vsip['TOTAL_LOSS'])

        # if new_vsip['TOTAL_LOSS'] == 1651:
        #     print()
        #     print(new_vsip['PATH'])
        #     print()

        return

    # Do not keep considering new_vsip if it has a total loss that is greater
    # or equal than the smallest that has already been shown to lead to all 
    # valves being open
    if new_vsip['TOTAL_LOSS'] >= min_total_loss:

        # if new_vsip['TOTAL_LOSS'] == 1651:
        #     print()
        #     print(new_vsip['PATH'])
        #     print()

        return

    valve_states__in_process.append(new_vsip)

    # TESTING ONLY .....
    # for i, vs in enumerate(valve_states__in_process):
        # print(f'{i}: {vs["PATH"]}')
    # print()
    # dummy = 123

valve_constants = dict()
valve_states__in_process = [dict()]
valve_states__finished = []

# This is defined to be the flow rate when all valves are open
max_flow_rate = 0

# This is defined to be the smallest total loss seen
min_total_loss = float('inf')

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        valve_constant = create_valve(in_string)
        valve_constants[valve_constant.name] = valve_constant
        max_flow_rate += int(in_string[23:].split(';')[0])
        if valve_constants[valve_constant.name].flow_rate > 0:
            valve_states__in_process[0][valve_constant.name] = ValveState.IS_CLOSED
        else:
            # Design decision: initially label valves with a flowrate of zero as "open"
            # (The program logic will choose whether or not to open valves with 
            # nonzero flowrate, and it will not bother wasting time on opening valves ]
            # with a zero flow rate.  This is because the goal is to maximize the total
            # pressure released in the first thirty minutes)
            valve_states__in_process[0][valve_constant.name] = ValveState.IS_OPEN

valve_states__in_process[0]['TOTAL_LOSS'] = 0
valve_states__in_process[0]['PATH'] = ['AA']
valve_states__in_process[0]['CURRENT_LOCATION'] = 'AA'

while len(valve_states__in_process) > 0:
    this_vsip = valve_states__in_process.pop()
    current_location = this_vsip['CURRENT_LOCATION']

    # TESTING ONLY !!!!!!!!
    see_if_match(this_vsip)

    for option in valve_constants[current_location].valves_via_tunnel:
        new_vsip = copy.deepcopy(this_vsip)
        new_vsip['CURRENT_LOCATION'] = option
        curr_flow_loss = max_flow_rate - get_flow_rate(new_vsip, valve_constants)
        new_vsip['TOTAL_LOSS'] += curr_flow_loss
        new_vsip['PATH'].append(option)
        special_append(new_vsip, valve_states__in_process, min_total_loss)

    if this_vsip[current_location] == ValveState.IS_CLOSED:
        new_vsip = copy.deepcopy(this_vsip)
        new_vsip[current_location] = ValveState.IS_OPEN

        curr_flow_loss = max_flow_rate - get_flow_rate(new_vsip, valve_constants)
        new_vsip['TOTAL_LOSS'] += curr_flow_loss
        new_vsip['PATH'].append('OPENED')
        
        # conditional on whether at least one valve (with a flowrate) remains closed
        if curr_flow_loss > 0:
            # inside function -- conditional on whether out of time ... based on len(new_vsip['PATH'])
            special_append(new_vsip, valve_states__in_process, min_total_loss)
        else:
            min_total_loss = min(min_total_loss, new_vsip['TOTAL_LOSS'])

            # TESTING  ADFOAWIERFASDFASFASDASDFAFASDFASODFASIDFJASDFASDFOISDFASDF
            # if new_vsip['PATH'][-1] == 'CC':
            # if new_vsip['TOTAL_LOSS'] < 1733:
            #     print()
            #     print(f'Total Loss: {new_vsip["TOTAL_LOSS"]}')
            #     print(new_vsip['PATH'])
            #     print()


print(f'The total loss is : {min_total_loss}')
print(f'The answer is {30 * max_flow_rate - min_total_loss}')
print('Path followed: ')
dummy = 123

