# adventOfCode 2022 day 7
# https://adventofcode.com/2022/day/7


class directory_structure:
    def __init__(self):
        self.current_directory = None

    def cd(self, directory_param):
        if directory_param == '/':
            self.current_directory = '/'
            return
        else:
            # Require that 'cd /' be the first statement !!!
            if self.current_directory is None:
                raise ValueError('You must run cd / before changing directory to anywhere else')
        raise(f'More code to be written to handle: cd {directory_param}')
ds = directory_structure()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    # for line_num, in_string in enumerate(f):
    for in_string in f:
        in_string = in_string.rstrip()

        print(in_string)

        # Handling a command passed to command line
        if in_string[:2] == '$ ':
            command_str, params_str = in_string[2:].split(' ')
            globals()[command_str](params_str)



        


