# adventOfCode 2022 day 8
# https://adventofcode.com/2022/day/8


forest = []

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        the_list = list(in_string)
        the_list = [int(x) for x in the_list]
        forest.append([{'height':x, 'visible':False, 'up_view':None, 'down_view':None, 'left_view':None, 'right_view':None} for x in the_list])


# Display trees
for i in range(len(forest)):
    for j in range(len(forest[0])):
        print(forest[i][j]['height'], end = ' ')
    print()
print()



# Travel along horizontal axis
for outer_axis in range(len(forest)):
    # look at vertical axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest[0])):
        if forest[outer_axis][inner_axis]['height'] > highest_seen:
            highest_seen = forest[outer_axis][inner_axis]['height']
            forest[outer_axis][inner_axis]['visible'] = True
    # look at vertical axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest[0]), -1):
        if forest[outer_axis][inner_axis]['height'] > highest_seen:
            highest_seen = forest[outer_axis][inner_axis]['height']
            forest[outer_axis][inner_axis]['visible'] = True 

# Travel along vertical axis
for outer_axis in range(len(forest[0])):
    # look at horizontal axis, ascending
    highest_seen = -1
    for inner_axis in range(len(forest)):
        if forest[inner_axis][outer_axis]['height'] > highest_seen:
            highest_seen = forest[inner_axis][outer_axis]['height']
            forest[inner_axis][outer_axis]['visible'] = True
    # look at horizontal axis, descending
    highest_seen = -1
    for inner_axis in range(-1, -1 - len(forest), -1):
    # for inner_axis in range(len(forest_heights)):
        if forest[inner_axis][outer_axis]['height'] > highest_seen:
            highest_seen = forest[inner_axis][outer_axis]['height']
            forest[inner_axis][outer_axis]['visible'] = True

# Count visible trees (and perhaps display them)
count_visible = 0
print('"True" below indicates that a tree is visible ... "False" indicates that it is invisible')
for i in range(len(forest)):
    for j in range(len(forest[0])):
        print(forest[i][j]['visible'], end = ' ')
        if forest[i][j]['visible']:
            print(' ', end='')
            count_visible += 1
    print()
print()
print(f'There are {count_visible} trees visible (answer to part A)\n')


