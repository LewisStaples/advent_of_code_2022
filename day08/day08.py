# adventOfCode 2022 day 8
# https://adventofcode.com/2022/day/8


forest_heights = []
forest_visible = []

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        the_list = list(in_string)
        the_list = [int(x) for x in the_list]
        forest_heights.append(the_list)

        forest_visible.append([False for x in range(len(the_list))])


# # Display trees
# for i in range(len(forest_heights)):
#     for j in range(len(forest_heights[0])):
#         print(forest_heights[i][j], end = ' ')
#     print()
# print()



# Travel along horizontal axis
for outer_axis in range(len(forest_heights)):
    # look at vertical axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest_heights[0])):
        if forest_heights[outer_axis][inner_axis] > highest_seen:
            highest_seen = forest_heights[outer_axis][inner_axis]
            forest_visible[outer_axis][inner_axis] = True
    # look at vertical axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest_heights[0]), -1):
        if forest_heights[outer_axis][inner_axis] > highest_seen:
            highest_seen = forest_heights[outer_axis][inner_axis]
            forest_visible[outer_axis][inner_axis] = True 
            dummy = 123

# Travel along vertical axis
for outer_axis in range(len(forest_heights[0])):
    # look at horizontal axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest_heights)):
        if forest_heights[inner_axis][outer_axis] > highest_seen:
            highest_seen = forest_heights[inner_axis][outer_axis]
            forest_visible[inner_axis][outer_axis] = True
    # look at horizontal axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest_heights), -1):
    # for inner_axis in range(len(forest_heights)):
        if forest_heights[inner_axis][outer_axis] > highest_seen:
            highest_seen = forest_heights[inner_axis][outer_axis]
            forest_visible[inner_axis][outer_axis] = True

# Count visible trees (and perhaps display them)
count_visible = 0
for i in range(len(forest_heights)):
    for j in range(len(forest_heights[0])):
        # print(forest_visible[i][j], end = ' ')
        if forest_visible[i][j]:
            # print(' ', end='')
            count_visible += 1
    # print()
# print()


print(f'There are {count_visible} trees visible (answer to part A)\n')


