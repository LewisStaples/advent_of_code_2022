# adventOfCode 2022 day 6
# https://adventofcode.com/2022/day/6


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
    print(f'{in_string}\n')
i = 4
while True:
    potential_substring = in_string[i-4:i]
    if len(set(potential_substring)) < 4:
        i += 1
    else:
        break
print(f'The answer to A is {i}\n')


