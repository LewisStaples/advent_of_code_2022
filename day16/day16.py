#!/usr/bin/env python3

# adventOfCode 2022 day 16
# https://adventofcode.com/2022/day/16

from dataclasses import dataclass

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


# This will contain input for all valves
valve_constants = dict()

# Contain distances (and paths required) to other valves  (? with nonzero flowrates ? )
valve_paths = dict()

# Reading input from the input file into valve_constants
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        valve_constant = create_valve(in_string)
        valve_constants[valve_constant.name] = valve_constant

del valve_constant, input_filename, in_string, f

# Convert valve_constants' data into valve_paths
for iv_count, init_valve in enumerate(valve_constants):
    child_transit_duration = 1
    # key: visited_valve identifier,  value: is transit duration for its child(ren)
    all_visited_valves = {init_valve: child_transit_duration}
    while len(all_visited_valves) < len(valve_constants):
        latest_valves = [k for k, v in all_visited_valves.items() if v == child_transit_duration]
        for latest_valve in latest_valves:
            for next_value in valve_constants[latest_valve].valves_via_tunnel:
                if next_value not in all_visited_valves:
                    all_visited_valves[next_value] = child_transit_duration + 1

        child_transit_duration += 1
    
    for dest_valve, duration in all_visited_valves.items():
        if valve_constants[dest_valve].flow_rate != 0:
            if init_valve != dest_valve:
                valve_paths[(init_valve, dest_valve)] = duration

dummy = 123





    



