# adventOfCode 2022 day 22
# https://adventofcode.com/2022/day/22


def get_input(input_filename):
    board_map = []
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        for line_num, in_string in enumerate(f):
            in_string = in_string.rstrip()
            this_line = list(in_string)
            if line_num == 0:
                board_map.append(list(' '*(len(in_string) + 2)))
            if len(this_line) > 0 and not this_line[0].isdigit():
                this_line.append(' ')
                this_line.insert(0, ' ')
                board_map.append(this_line)

    board_map.append(list(' '*len(board_map[-1])))

    return board_map, in_string
    
def solve_problem(input_filename):
    board_map, path = get_input(input_filename)


solve_problem('input.txt')

