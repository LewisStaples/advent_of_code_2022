# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_input_line(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
    print()
    
def solve_problem(input_filename):
    in_string = get_input_line(input_filename)

# solve_problem('input.txt')

def test_sample_0():
    solve_problem('input_sample0.txt')
    

# POTENTIAL ALTERNATIVE FOR SINGLE LINE INPUT FILES ....

def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input is: {in_string}')
    return in_string


def solve_problem(input_filename):
    in_string = get_input_line(input_filename)


solve_problem('input_sample0.txt')


# FOR SINGLE LINE INPUT FILES ....

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   
# Parsing input file   
print(in_string)



# FOR MULTILINE FILES .....

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)

