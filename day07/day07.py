# adventOfCode 2022 day 7
# https://adventofcode.com/2022/day/7


from enum import Enum


class Prompt_mode(Enum):
    COMMAND_MODE = 1  # Taking commands from the user
    LIST_MODE = 2  # Not taking commands from the user


class directory_structure:
    def __init__(self):
        self.current_directory = None
        self.prompt_mode = Prompt_mode.COMMAND_MODE
        self.directory_structure = dict()

    def cd(self, directory_param):
        if self.prompt_mode != Prompt_mode.COMMAND_MODE:
            raise ValueError(
                "Error: cd command is being run while in mode " + self.prompt_mode
            )
        if directory_param[0] == "/":
            # Change the directory to the given absolute path
            self.current_directory = directory_param
            return
        else:
            """Require that the current directory be known before
            attempting a relative change of directory"""
            if self.current_directory is None:
                raise ValueError(
                    "Error: you must specify the absolute path "
                    + "before making a relative change to the path"
                )

        if directory_param == "..":
            if self.current_directory[-1] != "/":
                raise ValueError(
                    "Error: trying to cd .. against this directory: "
                    + self.current_directory
                )
            self.current_directory = self.current_directory[:-1]
            index_last_slash = self.current_directory.rfind("/")
            self.current_directory = self.current_directory[: index_last_slash + 1]
        else:
            self.current_directory += directory_param + "/"

    def ls(self, params):
        assert params is None
        if self.current_directory in self.directory_structure:
            return
        # implicit else ... fill in the directory's contents
        self.directory_structure[self.current_directory] = dict()
        self.prompt_mode = Prompt_mode.LIST_MODE

    def new_listing(self, input_line):
        item_characteristic, item_name = input_line.split(" ")
        if item_characteristic == "dir":
            item_type = "dir"
        else:
            item_type = "file"
        self.directory_structure[self.current_directory][item_name] = {
            "item_type": item_type
        }
        if item_type == "file":
            self.directory_structure[self.current_directory][item_name][
                "file_size"
            ] = int(item_characteristic)


ds = directory_structure()

# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    for in_string in f:
        in_string = in_string.rstrip()
        # Handling a command passed to command line
        if in_string[:2] == "$ ":
            ds.prompt_mode = Prompt_mode.COMMAND_MODE
            in_string = in_string[2:]
            if " " in in_string:
                command_str, params_str = in_string.split(" ")
            else:
                command_str = in_string
                params_str = None
            method_to_run = getattr(ds, command_str)
            method_to_run(params_str)
        else:
            if ds.prompt_mode == Prompt_mode.LIST_MODE:
                ds.new_listing(in_string)


def get_total_sizes(path):
    ret_val = {path: 0}
    for name, v in ds.directory_structure[path].items():
        if v["item_type"] == "file":
            ret_val[path] += v["file_size"]
        elif v["item_type"] == "dir":
            ret_val |= get_total_sizes(
                path + name + "/"
            )  # |= operator added in Python 3.9
            ret_val[path] += ret_val[path + name + "/"]
    return ret_val


# Now solve the part A problem
directories_total_sizes = get_total_sizes("/")
total_dirs_at_most_100k = 0
for i, k in directories_total_sizes.items():
    if k <= 100000:
        total_dirs_at_most_100k += k
print(
    f"The answer for part A: total sizes of all directories {total_dirs_at_most_100k}\n"
)

# Now solve the part B problem
filesize_to_delete = 30000000 + directories_total_sizes["/"] - 70000000
for size in sorted(directories_total_sizes.values()):
    if size >= filesize_to_delete:
        print(f"The answer for part B:  {size}")
        print("(This is the filesize of smallest directory that will suffice)\n")
        break
