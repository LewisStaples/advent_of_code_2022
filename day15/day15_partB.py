#!/usr/bin/env python3

# adventOfCode 2022 day 15
# https://adventofcode.com/2022/day/15

# The big picture here is that it is defined that there is only one point in this given
# range that could be a beacon that wasn't prevoiusly known.  If there were a unknown
# beacon that was more than 1 unit outside the manhattan distance of any sensor,
# then there must be another unknown beacon that's one unit closer
# ... thus failing the requirement that there be only one unknown beacon.


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
        print(f"{y:3}", end=":  ")
        for x in range(
            int(sensor.real) - manh_dist - 1, int(sensor.real) + manh_dist + 2
        ):
            point = x + y * 1j
            if point == sensor:
                print("S", end="")
            elif point == beacon:
                print("B", end="")
            elif point in diamond_points:
                print("*", end="")
            else:
                print("-", end="")
        print()
    print("\n")


def get_diamond_points(sensor, manh_dist, x_y_range):
    ret_val = set()
    y_lower = max(x_y_range[0], int(sensor.imag) - manh_dist - 1)
    y_upper = min(x_y_range[1], int(sensor.imag) + manh_dist + 1)
    for y in range(y_lower, y_upper + 1):
        x_diff = manh_dist + 1 - abs(y - sensor.imag)
        if sensor.real - x_diff >= x_y_range[0]:
            if sensor.real - x_diff <= x_y_range[1]:
                ret_val.add(sensor.real - x_diff + y * 1j)
        if sensor.real + x_diff >= x_y_range[0]:
            if sensor.real + x_diff <= x_y_range[1]:
                ret_val.add(sensor.real + x_diff + y * 1j)

    return ret_val


def its_the_distress_beacon(point, all_sensors_with_manh_dist):
    for this_sensor in all_sensors_with_manh_dist:
        if (
            get_manhattan_distance(point, this_sensor)
            <= all_sensors_with_manh_dist[this_sensor]
        ):
            return False
    # If False hasn't been returned for any sensor for this point,
    # then this point is the one
    return True


def point_display(point):
    return f"({int(point.real)}, {int(point.imag)})"


def tuning_frequency(point):
    return int(point.real) * 4000000 + int(point.imag)


# End of function declarations
# Start of main program logic

# Select input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
if input_filename == "input_sample0.txt":
    x_y_range = [0, 20]
else:
    x_y_range = [0, 4000000]

all_sensors_with_manh_dist = dict()
all_diamond_points = set()
all_beacons = set()

# Read input and process the data
with open(input_filename) as f:
    # Pull in each line from the input file
    for linenum, in_string in enumerate(f):
        print(in_string, end="")
        sensor, beacon = get_devices_from_input_line(in_string)
        all_sensors_with_manh_dist[sensor] = get_manhattan_distance(sensor, beacon)
        # these_diamond_points are the "diamond points" associated with one sensor.
        # The "diamond points" all manh_dist + 1 away from its associated sensor,
        # where manh_dist is the manh_dist to the sensor's nearest visible beacon.
        # Note that the "diamond points," as defined her in the program,
        # also are required to be in the permissible range of x, y values
        # (for the real problem, this range is [0, 4000000].
        # Whereas for the example, the upper limit is 20)
        these_diamond_points = get_diamond_points(
            sensor, all_sensors_with_manh_dist[sensor], x_y_range
        )
        display(sensor, beacon, these_diamond_points)
        # all_diamond_points are the "diamond points" associated with all sensors
        all_diamond_points.update(these_diamond_points)
        all_beacons.add(beacon)

for point in all_diamond_points:
    if its_the_distress_beacon(point, all_sensors_with_manh_dist):
        print(f"The distress beacon is {point_display(point)}")
        print(f"The answer to part B is:  {tuning_frequency(point)}")
print()
