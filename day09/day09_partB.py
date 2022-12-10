# adventOfCode 2022 day 9
# https://adventofcode.com/2022/day/9


import numpy as np
import math


def is_touching(head_location, tail_location):
    """
    If any edge had length 2 or greater than the calculation would be at least two.
    The calculation would be exactly one, if one edge had length 1 and the other 0
    The calculation would be sqrt(2) if both edges had length of one

    To protect against round-off error, 1.5 is used because it's greater than sqrt(2) ~ 1.414
    """
    if math.dist(head_location, tail_location) < 1.5:
        return True


def get_new_tail_location(head_location, tail_location):
    if is_touching(head_location, tail_location):
        return tail_location
    # If the difference is two in any direction, use the midpoint as the new tail
    if math.dist(head_location, tail_location) < 2.1:
        return (head_location + tail_location) // 2
    for movement in [
        np.array([1, 1]),
        np.array([1, -1]),
        np.array([-1, 1]),
        np.array([-1, -1]),
    ]:
        new_tail_location = tail_location + movement
        if is_touching(head_location, new_tail_location):
            return new_tail_location
    raise (
        ValueError(
            f"ERROR: Cannot find new tail for given head/tail combination: {head_location}, {tail_location}"
        )
    )


knots_locations = []
for i in range(10):
    knots_locations.append(np.array([0, 0]))
direction_coords = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}
all_tail_points = set()

# Reading input from the input file
input_filename = "input_sample1.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        direction, distance = in_string.split(" ")
        distance = int(distance)
        for i in range(distance):
            knots_locations[0] += direction_coords[direction]
            for i in range(1, 10):
                knots_locations[i] = get_new_tail_location(
                    knots_locations[i - 1], knots_locations[i]
                )
            all_tail_points.add(tuple(knots_locations[-1]))

print(
    f"Total number of positions visited by tail (answer to B) is {len(all_tail_points)}\n"
)
