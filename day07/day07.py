# adventOfCode 2022 day 7
# https://adventofcode.com/2022/day/7


from enum import Enum

class Prompt_mode(Enum):
    COMMAND_MODE = 1
    LIST_MODE = 2
class directory_structure:
    def __init__(self):
        self.current_directory = None
        self.mode = Prompt_mode.COMMAND_MODE

    def cd(self, directory_param):
        if self.mode != Prompt_mode.COMMAND_MODE:
            raise ValueError('Error: cd command is being run while in mode ' + self.mode)
        if directory_param == '/':
            self.current_directory = '/'
            return
        else:
            # Require that 'cd /' be the first statement !!!
            if self.current_directory is None:
                raise ValueError('Error: you must run cd / before changing directory to anywhere else')

        if directory_param == '..':
            if self.current_directory[-1] is not '/':
                raise ValueError('Error: trying to cd .. against this directory: ' + self.current_directory)
            self.current_directory = self.current_directory[:-1]
            index_last_slash = self.current_directory.rfind('/')
            self.current_directory = self.current_directory[:index_last_slash + 1]
        else:
            self.current_directory += directory_param + '/'
        
        dummy = 123

    def ls(self, params):
        assert params is None

        dummy = 123


ds = directory_structure()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    for in_string in f:
        in_string = in_string.rstrip()

        print(in_string)

        # Handling a command passed to command line
        if in_string[:2] == '$ ':
            in_string = in_string[2:]
            if ' ' in in_string:
                command_str, params_str = in_string.split(' ')
            else:
                command_str = in_string
                params_str = None
            method_to_run = getattr(ds, command_str)
            method_to_run(params_str)



        


