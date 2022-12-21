# adventOfCode 20xy day 20
# https://adventofcode.com/20xy/day/20

from dataclasses import dataclass

@dataclass
class Number:
    number: int
    def __str__(self):
        return str(self.number)

def print_list(number_list):
    if len(number_list) < 10:
        print('[', end='')
        for the_number in number_list:
            print(the_number, end=',')
        print(']\n')

def get_number_list(input_filename, number_list, number_lookup):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for the_index, in_string in enumerate(f):
            in_string = in_string.rstrip()
            number_list.append(Number(int(in_string)))
            number_lookup[the_index] = number_list[-1]
            if number_list[-1].number == 0:
                zero_number = number_list[-1]
    print_list(number_list) # (the fxn only prints if its short enough)
    return zero_number
    

def solve_problem(input_filename):
    number_list = list()
    number_lookup = dict()
    zero_number = get_number_list(input_filename, number_list, number_lookup)

solve_problem('input_sample0.txt')

