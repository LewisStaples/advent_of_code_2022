# adventOfCode 2022 day 03
# https://adventofcode.com/2022/day/03


sum_priorities = 0

priority_dict = dict()
for i in range(26):
    priority_dict[chr(ord("a") + i)] = i + 1
    priority_dict[chr(ord("A") + i)] = i + 27


# Reading input from the input file
input_filename = "input.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    looking_for_badge = set()
    for line_number, in_string in enumerate(f):
        in_string = in_string.rstrip()
        if line_number % 3 == 0:
            looking_for_badge = set(in_string)
        else:
            looking_for_badge = looking_for_badge.intersection(set(in_string))
        if line_number % 3 == 2:
            sum_priorities += priority_dict[looking_for_badge.pop()]
            looking_for_badge = set()


print(f"The answer to part B is {sum_priorities}\n")
