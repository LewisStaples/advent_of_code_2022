# adventOfCode 2022 day 22
# https://adventofcode.com/2022/day/22


import numpy as np

class Location:
    directions = {
        0: np.array([0,1]),
        1: np.array([1,0]),
        2: np.array([0,-1]),
        3: np.array([-1,0]),
    }
    def __init__(self, column_number):
        self.direction = 0
        self.location = np.array([1, column_number])
    
    def rotate(self, ch):
        if ch == 'R':
            self.direction = (self.direction + 1) % len(Location.directions)
        elif ch == 'L':
            self.direction = (self.direction - 1) % len(Location.directions)
        else:
            raise ValueError(f'rotate called with {ch}')
        
    def go(self, distance, board_map):
        for i in range(distance):
            # original_location = self.location
            new_location = self.location + Location.directions[self.direction]

            if board_map[new_location[0]][new_location[1]] in ['#',' ']:
                return

            # implicit else
            self.location = new_location


class Path:
    def __init__(self, path_str):
        self.path_str = path_str
        self.str_index = 0
    
    def get_next_datum(self):
        if self.str_index == len(self.path_str):
            return None # flag to indicate the path is complete
        if self.path_str[self.str_index] in ['L', 'R']:
            self.str_index += 1
            return self.path_str[self.str_index - 1]
        if self.path_str[self.str_index].isdigit():
            ret_val = self.path_str[self.str_index]
            while self.str_index < len(self.path_str) - 1:
                # self.str_index += 1
                if self.path_str[self.str_index + 1].isdigit():
                    # self.path_str[self.str_index]
                    ret_val += self.path_str[self.str_index + 1]
                    self.str_index += 1
                else:
                    break
            self.str_index += 1
            return int(ret_val)
        raise(f'Failing to read path at index {self.str_index}: full_path: {self.path_str}')

def get_input(input_filename):
    initial_position = None
    board_map = []
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_num, in_string in enumerate(f):
            in_string = in_string.rstrip()
            this_line = list(in_string)
            if line_num == 0:
                board_map.append(list(' '*(len(in_string) + 2)))
                initial_position = Location(
                    in_string.index('.') + 1
                )
            if len(this_line) > 0 and not this_line[0].isdigit():
                this_line.append(' ')
                this_line.insert(0, ' ')
                board_map.append(this_line)
    board_map.append(list(' '*len(board_map[-1])))
    if len(in_string) < 20:
        print(f'Path: {in_string}\n')
    return board_map, in_string, initial_position

def get_final_position(board_map, path_str, the_location):
    path_object = Path(path_str)

    next_datum = 'dummy_value'
    while True:
        next_datum = path_object.get_next_datum()
        if next_datum is None:
            break
        print(f'next_datum: {next_datum}')
        if isinstance(next_datum, int):
            the_location.go(next_datum, board_map)
            # continue
        elif next_datum not in ['L', 'R']:
            raise ValueError(f'Bad datum {next_datum} in path: {path_str}')
        else:
            the_location.rotate(next_datum)

        dummy = 123

    return the_location


def solve_problem(input_filename):
    board_map, path_str, the_location = get_input(input_filename)
    the_location = get_final_position(board_map, path_str, the_location)

solve_problem('input_sample0.txt')

