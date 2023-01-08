#!/usr/bin/env python3

# adventOfCode 2022 day 15
# https://adventofcode.com/2022/day/15


def get_point_from_input_line_snippet(in_snippet):
    point = in_snippet.split(", ")
    point = [int(x[2:]) for x in point]
    return point


def get_devices_from_input_line(in_string):
    in_string = in_string.rstrip()
    point_pair = in_string.split(": closest beacon is at ")
    return get_point_from_input_line_snippet(
        point_pair[0][10:]
    ), get_point_from_input_line_snippet(point_pair[1])


def get_manhattan_distance(point1, point2):
    ret_val = 0
    for i in range(len(point1)):
        ret_val += abs(point1[i] - point2[i])
    return ret_val


def display(sensor, beacon, points_not_beacons__this_call, row_of_interest):
    if row_of_interest > 50:
        return

    manh_dist = get_manhattan_distance(sensor, beacon)
    print(f"Sensor: {sensor}, Beacon: {beacon}\n")
    for y in range(sensor[1] - manh_dist - 1, sensor[1] + manh_dist + 2):
        print(f"{y:2}", end=":  ")
        for x in range(sensor[0] - manh_dist, sensor[0] + manh_dist + 1):
            if (x, y) == sensor:
                print("S", end="")
            elif [x, y] == beacon:
                print("B", end="")
            elif get_manhattan_distance(sensor, [x, y]) <= manh_dist:
                print("*", end="")
            else:
                print("?", end="")
        if y == row_of_interest:
            print("  ---  ROW OF INTEREST")
        else:
            print()
    print()
    print(
        f"x-values of points that cannot be beacons discovered in the row of interest: \
{points_not_beacons__this_call}"
    )
    print("\n")


def record_non_beacon_points(sensor, beacon, points_not_beacons, row_of_interest):
    # Treating this as a separate variable,
    # so I can display the findings from this particular step
    points_not_beacons__this_call = set()

    # Find all points within the manhattan distance of the sensor
    manh_dist = get_manhattan_distance(sensor, beacon)
    for x in range(
        sensor[0] - manh_dist + abs(row_of_interest - sensor[1]),
        sensor[0] + manh_dist + 1 - abs(row_of_interest - sensor[1]),
    ):
        points_not_beacons__this_call.add(x)

    # Remove the beacon if it got added in the above code.
    # If a beacon is there, it must not be listed as a non-beacon point
    if beacon[1] == row_of_interest:
        points_not_beacons__this_call.discard(beacon[0])

    # Display sensor, beacon, points_not_beacons (if small enough)
    display(sensor, beacon, points_not_beacons__this_call, row_of_interest)

    points_not_beacons.update(points_not_beacons__this_call)


# Select input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")


# The row of interest depends on which input file is used
if input_filename in ["input_sample0.txt", "input_scenario0.txt"]:
    row_of_interest = 10
elif input_filename == "input.txt":
    row_of_interest = 2000000

points_not_beacons = set()

# Read input and process the data
with open(input_filename) as f:
    # Pull in each line from the input file
    for linenum, in_string in enumerate(f):
        sensor, beacon = get_devices_from_input_line(in_string)
        record_non_beacon_points(sensor, beacon, points_not_beacons, row_of_interest)

if row_of_interest < 50:
    print(points_not_beacons)
print(f"The answer to part 1 / part A is:  {len(points_not_beacons)}\n")
