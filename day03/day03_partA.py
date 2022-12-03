# adventOfCode 2022 day 03
# https://adventofcode.com/2022/day/03


sum_priorities = 0

priority_dict = dict()
for i in range(26):
    dummy = 123
    priority_dict[chr(ord("a") + i)] = i + 1
    priority_dict[chr(ord("A") + i)] = i + 27

# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        left_side = set(in_string[0 : len(in_string) // 2])
        right_side = set(in_string[len(in_string) // 2 :])
        shared_item = left_side.intersection(right_side)
        sum_priorities += priority_dict[shared_item.pop()]

print(f"The answer to part A is {sum_priorities}\n")
