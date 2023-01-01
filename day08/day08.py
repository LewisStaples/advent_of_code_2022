#!/usr/bin/env python3

# adventOfCode 2022 day 8
# https://adventofcode.com/2022/day/8


forest = []

# Reading input from the input file
input_filename = "input.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        the_list = list(in_string)
        the_list = [int(x) for x in the_list]
        forest.append(
            [
                {
                    "height": x,
                    "visible": False,
                    "up_view": None,
                    "down_view": None,
                    "left_view": None,
                    "right_view": None,
                }
                for x in the_list
            ]
        )


# Display trees (if the forest is small enough)
if len(forest) < 10:
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            print(forest[i][j]["height"], end=" ")
        print()
    print()


# Travel along vertical axis
for outer_axis in range(len(forest)):
    # look at horizontal axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest[0])):
        if forest[outer_axis][inner_axis]["height"] > highest_seen:
            highest_seen = forest[outer_axis][inner_axis]["height"]
            forest[outer_axis][inner_axis]["visible"] = True
    # look at horizontal axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest[0]), -1):
        if forest[outer_axis][inner_axis]["height"] > highest_seen:
            highest_seen = forest[outer_axis][inner_axis]["height"]
            forest[outer_axis][inner_axis]["visible"] = True
# Travel along horizontal axis
for outer_axis in range(len(forest[0])):
    # look at vertical axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest)):
        if forest[inner_axis][outer_axis]["height"] > highest_seen:
            highest_seen = forest[inner_axis][outer_axis]["height"]
            forest[inner_axis][outer_axis]["visible"] = True
    # look at vertical axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest), -1):
        if forest[inner_axis][outer_axis]["height"] > highest_seen:
            highest_seen = forest[inner_axis][outer_axis]["height"]
            forest[inner_axis][outer_axis]["visible"] = True

# Count visible trees (and perhaps display them)
count_visible = 0
for i in range(len(forest)):
    for j in range(len(forest[0])):
        if forest[i][j]["visible"]:
            count_visible += 1
print(f"There are {count_visible} trees visible (answer to part A)\n")

# Travel along vertical axis
for outer_axis in range(1, len(forest) - 1):
    # look at horizontal axis, ascending
    # key -- height of observer tree,
    # value -- coordinate of farthest tree that can be seen
    index_of_farthest_visible_tree = {x: 0 for x in range(0, 10)}
    for inner_axis in range(1, len(forest[0]) - 1):
        tree_height = forest[outer_axis][inner_axis]["height"]

        forest[outer_axis][inner_axis]["left_view"] = (
            inner_axis - index_of_farthest_visible_tree[tree_height]
        )

        for height in range(0, tree_height + 1):
            index_of_farthest_visible_tree[height] = inner_axis

    # look at vertical axis, descending
    index_of_farthest_visible_tree = {x: (len(forest[0]) - 1) for x in range(0, 10)}
    for inner_axis in range(len(forest[0]) - 2, 0, -1):
        tree_height = forest[outer_axis][inner_axis]["height"]
        forest[outer_axis][inner_axis]["right_view"] = (
            index_of_farthest_visible_tree[tree_height] - inner_axis
        )
        for height in range(0, tree_height + 1):
            index_of_farthest_visible_tree[height] = inner_axis

# Travel along horizontal axis
for outer_axis in range(1, len(forest[0]) - 1):
    # look at vertical axis, ascending
    index_of_farthest_visible_tree = {x: 0 for x in range(0, 10)}
    for inner_axis in range(1, len(forest) - 1):
        tree_height = forest[inner_axis][outer_axis]["height"]
        forest[inner_axis][outer_axis]["up_view"] = (
            inner_axis - index_of_farthest_visible_tree[tree_height]
        )
        for height in range(0, tree_height + 1):
            index_of_farthest_visible_tree[height] = inner_axis

    # look at vertical axis, descending
    index_of_farthest_visible_tree = {x: (len(forest) - 1) for x in range(0, 10)}
    for inner_axis in range(len(forest) - 2, 0, -1):
        tree_height = forest[inner_axis][outer_axis]["height"]
        forest[inner_axis][outer_axis]["down_view"] = (
            index_of_farthest_visible_tree[tree_height] - inner_axis
        )
        for height in range(0, tree_height + 1):
            index_of_farthest_visible_tree[height] = inner_axis

# Find largest scenic score (answer to part B):
max_scenic_score = 0
for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[0]) - 1):
        tree = forest[y][x]
        max_scenic_score = max(
            max_scenic_score,
            tree["up_view"]
            * tree["down_view"]
            * tree["left_view"]
            * tree["right_view"],
        )

print(f"The largest scenic score is {max_scenic_score} (answer to part B)\n")
