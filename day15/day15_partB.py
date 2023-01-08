#!/usr/bin/env python3

# adventOfCode 2022 day 15
# https://adventofcode.com/2022/day/15

# Input one line at a time
#    Collect most points in a set of complex numbers that are one unit outside its Manh. Distance
#        Reason for most ... exclude those with (x,y) outside the given range
#    Come up with a data structure to determine if any points are inside that line's ring/diamond

# After all lines have been entered
#    Visit all points one unit outside above, one at a time
#    Determine if that point might or might not be a beacon by seeing if it is inside of any the rings/diamonds


def get_point_from_input_line_snippet(in_snippet):
    point = in_snippet.split(", ")
    return int(point[0][2:]) + int(point[1][2:]) * 1j


def get_devices_from_input_line(in_string):
    in_string = in_string.rstrip()
    point_pair = in_string.split(": closest beacon is at ")
    return get_point_from_input_line_snippet(
        point_pair[0][10:]
    ), get_point_from_input_line_snippet(point_pair[1])


def get_manhattan_distance(point1, point2):
    ret_val = 0
    ret_val += abs(point1.real - point2.real)
    ret_val += abs(point1.imag - point2.imag)
    return int(ret_val)

def display(sensor, beacon, diamond_points):
    if len(diamond_points) > 1000:
        return
    manh_dist = get_manhattan_distance(sensor, beacon)
    print(f"Sensor: {sensor}, Beacon: {beacon}\n")
    for y in range(int(sensor.imag) - manh_dist - 1, int(sensor.imag) + manh_dist + 2):
        print(f"{y:2}", end=":  ")
        for x in range(int(sensor.real) - manh_dist - 1, int(sensor.real) + manh_dist + 2):
            point = x + y*1j
            if point == sensor:
                print("S", end="")
            elif point == beacon:
                print("B", end="")
            # elif get_manhattan_distance(sensor, point) == manh_dist + 1:
            elif point in diamond_points:
                print("*", end="")
            else:
                print("-", end="")
        print()
    print('\n')

def get_diamond_points(sensor, beacon):
    # return set()
    ret_val = set()
    manh_dist = get_manhattan_distance(sensor, beacon)
    for y in range(int(sensor.imag) - manh_dist - 1, int(sensor.imag) + manh_dist + 2):
        x_diff = manh_dist + 1 - abs(y - sensor.imag)
        ret_val.add(sensor.real - x_diff + y*1j)
        ret_val.add(sensor.real + x_diff + y*1j)

    return ret_val

# Select input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")

# Read input and process the data
with open(input_filename) as f:
    # Pull in each line from the input file
    for linenum, in_string in enumerate(f):
        print(in_string, end = '')
        sensor, beacon = get_devices_from_input_line(in_string)
        diamond_points = get_diamond_points(sensor, beacon)
        display(sensor, beacon, diamond_points)

