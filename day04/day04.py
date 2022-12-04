# adventOfCode 2022 day 4
# https://adventofcode.com/2022/day/4

# Used https://pypi.org/project/portion/
# to handle intervals
import portion as P

count_fully_contained = 0
count_any_overlap = 0
# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        # Get left and right intervals
        in_string = in_string.rstrip()
        left_int_str, right_int_str = in_string.split(",")
        left_int_chars = left_int_str.split("-")
        left_int = P.closed(int(left_int_chars[0]), int(left_int_chars[1]))
        right_int_chars = right_int_str.split("-")
        right_int = P.closed(int(right_int_chars[0]), int(right_int_chars[1]))
        # Does this contribute to part A? (uses union interval)
        union_int = left_int | right_int
        if union_int == left_int or union_int == right_int:
            count_fully_contained += 1
        # Does this contribute to part B?
        if left_int.overlaps(right_int):
            count_any_overlap += 1

print(f"The answer to A is {count_fully_contained}\n")
print(f"The answer to B is {count_any_overlap}\n")
