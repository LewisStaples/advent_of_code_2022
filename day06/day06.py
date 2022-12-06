# adventOfCode 2022 day 6
# https://adventofcode.com/2022/day/6


# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file {input_filename}, which contains: ")
with open(input_filename) as f:
    in_string = f.readline().rstrip()
    print(f"{in_string[:50]}", end="")
    if len(in_string) > 50:
        print(f" ... ; total length: {len(in_string)}")
    print("\n")


def calc_start(starter_name, object_size):
    object_counter = 4
    while True:
        potential_substring = in_string[object_counter - object_size : object_counter]
        if len(set(potential_substring)) < object_size:
            object_counter += 1
        else:
            break
    print(
        f"Answer: {object_counter} characters need to be processed before the start of \
the first start-of-{starter_name} marker is processed.\n"
    )


calc_start("packet", 4)
calc_start("message", 14)
