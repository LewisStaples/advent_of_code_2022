# adventOfCode 2022 day 14
# https://adventofcode.com/2022/day/14


def convert_pointstr_to_point(pointstr):
    point = pointstr.split(',')
    point = [int(x) for x in point]
    return point

def add_points(rock_locations, point1, point2):
    if point1[0] == point2[0]:
        variable_index = 1
    else:
        variable_index = 0
    var_min = min(point1[variable_index], point2[variable_index])
    var_max = max(point1[variable_index], point2[variable_index])
    for the_value in range(var_min, var_max + 1):
        point1[variable_index] = the_value
        rock_locations.add(tuple(point1))


def add_edge(rock_locations, rock_path_nodes, i):
    point1 = convert_pointstr_to_point(rock_path_nodes[i])
    point2 = convert_pointstr_to_point(rock_path_nodes[i+1])
    add_points(rock_locations, point1, point2)

def get_rock_locations(input_filename):
    rock_locations = set()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            rock_path_nodes = in_string.split(' -> ')
            for i in range(len(rock_path_nodes) - 1):
                add_edge(rock_locations, rock_path_nodes, i)
    return rock_locations
    
def get_rock_boundaries(rock_locations):
    ret_val = {'highest_0': float('-inf'), 'lowest_0': float('inf'), 'highest_1': float('-inf'), 'lowest_1': float('inf')}
    for location in rock_locations:
        ret_val['highest_0'] = max(ret_val['highest_0'], location[0])
        ret_val['lowest_0'] = min(ret_val['lowest_0'], location[0])
        ret_val['highest_1'] = max(ret_val['highest_1'], location[1])
        ret_val['lowest_1'] = min(ret_val['lowest_1'], location[1])
    return ret_val

def display(rock_locations, sand_locations):
    print(f'Sand count: {len(sand_locations)}')
    if len(rock_locations) > 25:
        return
    rock_boundaries = get_rock_boundaries(rock_locations)
    for y in range(0, rock_boundaries['highest_1'] + 1):
        print(f'{y}  ', end = '')
        for x in range(rock_boundaries['lowest_0'], rock_boundaries['highest_0'] + 1):
            the_location = (x,y)
            if the_location in rock_locations:
                print('#', end = '')
            elif the_location in sand_locations:
                print('O', end = '')
            elif the_location == (500, 0):
                print('+', end = '')
            else:
                print('.', end = '')
        print()
    print()

def drop_sand_get_count(rock_locations, rock_boundaries):
    sand_locations = set()
    # location_size_start = len(rock_locations)
    while True:
        sand_unit = [500, 0]
        while True:
            next_potential_sand_units = []
            next_potential_sand_units.append([sand_unit[0], sand_unit[1] + 1])
            next_potential_sand_units.append([sand_unit[0] - 1, sand_unit[1] + 1])
            next_potential_sand_units.append([sand_unit[0] + 1, sand_unit[1] + 1])

            for next_sand_unit in next_potential_sand_units:
                if tuple(next_sand_unit) not in rock_locations.union(sand_locations):
                    sand_unit = next_sand_unit
                    if sand_unit[1] > rock_boundaries['highest_1']:
                        display(rock_locations, sand_locations)
                        return len(sand_locations) # this sand unit is falling endlessly
                    # found one of the three, so break from for loop 
                    # (because I/ you don't need to consider any of the others)
                    break 
            if sand_unit != next_sand_unit:
                display(rock_locations, sand_locations)
                sand_locations.add(tuple(sand_unit))
                break # None of the three options worked, so time to get another unit of sand


def solve_problem(input_filename):
    rock_locations = get_rock_locations(input_filename)
    rock_boundaries = get_rock_boundaries(rock_locations)

    # Drop sand
    print(f'\nAnswer to A: {drop_sand_get_count(rock_locations, rock_boundaries)}\n')

solve_problem('input_sample0.txt')

#
    




