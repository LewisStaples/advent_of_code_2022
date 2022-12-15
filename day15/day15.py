# adventOfCode 2022 day 15
# https://adventofcode.com/2022/day/15


# For each line of input
# Calculate the manhattan distance
# Determine the interval of positions on the given y-axis that cannot contain a beacon, for that line of input
# Add this interval to the intersection of intervals

def get_point_from_input(in_snippet):
    point = in_snippet.split(', ')
    point = [int(x[2:]) for x in point]
    return point

def get_devices_from_input_line(in_string):
    in_string = in_string.rstrip()
    point_pair = in_string.split(': closest beacon is at ')
    # print(in_string)
    return get_point_from_input(point_pair[0][10:]), get_point_from_input(point_pair[1])

def get_manhattan_distance(point1, point2):
    ret_val = 0
    for i in range(len(point1)):
        ret_val += abs(point1[i] - point2[i])
    return ret_val


# Select input file
input_filename='input_scenario0.txt'
print(f'\nUsing input file: {input_filename}\n')

# The row of interest depends on which input file is used
if input_filename in ['input_sample0.txt','input_scenario0.txt']:
    row_of_interest = 10
elif input_filename == 'input.txt':
    row_of_interest = 2000000

# Read input and process the data
with open(input_filename) as f:
    # Pull in each line from the input file
    for linenum, in_string in enumerate(f):
        sensor, beacon = get_devices_from_input_line(in_string)
        manhattan_distance = get_manhattan_distance(sensor, beacon)

def test_get_manhattan_distance_0():
    assert get_manhattan_distance([2,18], [-2,15]) == 7

def test_get_manhattan_distance_1():
    assert get_manhattan_distance([8,7], [2,10]) == 9


