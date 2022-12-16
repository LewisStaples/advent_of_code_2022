# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16


from dataclasses import dataclass

@dataclass
class Valve:
    name: str
    flow_rate: int
    valves_via_tunnel: list


def create_valve(in_string):
    return Valve(
        in_string[6:8], 
        int(in_string[in_string.index('=')+1:in_string.index(';')]),    
        in_string[9 + in_string.index('to valve'):].strip().split(', ')
    )

valve_data = dict()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # the_index = in_string[6:8]
        the_valve = create_valve(in_string)
        valve_data[the_valve.name] = the_valve

