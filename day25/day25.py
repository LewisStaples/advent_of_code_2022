# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_input_line(input_filename):
    decimal_value_list = []
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            decimal_value = 0
            for str_index, ch in enumerate(in_string):
                digit_value = {'2':2, '1':1, '0':0, '-':-1, '=':-2}[in_string[str_index]]
                decimal_value += digit_value * 5 ** (len(in_string) - str_index - 1)
            decimal_value_list.append(decimal_value)

            print(decimal_value)
            print()
    print()

    return decimal_value_list
    
def solve_problem(input_filename):
    decimal_value_list = get_input_line(input_filename)
    print(f'The total in decimal is {sum(decimal_value_list)}')

solve_problem('input_sample0.txt')

