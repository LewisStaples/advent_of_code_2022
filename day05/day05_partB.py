# adventOfCode 2022 day 5
# https://adventofcode.com/2022/day/5


stacks = dict()


def add_char_to_stacks(ch, index_num):
    stack_num = index_num - 1
    stack_num //= 4
    stack_num += 1
    if not ch.isalpha():
        return
    if stack_num not in stacks:
        stacks[stack_num] = []
    stacks[stack_num].append(ch)


# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        if "[" in in_string:
            # This line is one that defines initial state of the stacks of crates
            i_ch = 1
            while True:
                try:
                    add_char_to_stacks(in_string[i_ch], i_ch)
                except IndexError:
                    break
                i_ch += 4
        elif "move" in in_string:
            # This line is a move command
            in_string = in_string[5:]
            quantity_string, in_string = in_string.split(" from ")
            from_string, to_string = in_string.split(" to ")
            quantity_int = int(quantity_string)
            from_int = int(from_string)
            to_int = int(to_string)

            dummy = 123

            for i in range(quantity_int):
                stacks[to_int].insert(i, stacks[from_int].pop(0))

                dummy = 123

        else:
            # This line will be ignored
            continue

print("\nThe answer to part A is: ", end="")
for i in range(1, len(stacks) + 1):
    if len(stacks[i]) > 0:
        print(stacks[i][0], end="")
print("\n")
