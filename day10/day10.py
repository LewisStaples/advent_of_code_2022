# adventOfCode 20xy day 10
# https://adventofcode.com/2022/day/10


def update_recorded_values(recorded_values, cycle_number, x_register):
    if cycle_number in recorded_values:
        recorded_values[cycle_number] = x_register

# reset to 1 when first instruction is read
cycle_number = 0
x_register = 1
recorded_values = {20: None, 60: None, 100: None, 140: None, 180: None,220: None}

input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    for in_string in f:
        cycle_number += 1
        update_recorded_values(recorded_values, cycle_number, x_register)
        in_string = in_string.rstrip()
        if in_string[:4] == 'addx':
            cycle_number += 1
            update_recorded_values(recorded_values, cycle_number, x_register)
            x_register += int(in_string[5:])
sum_of_signal_strengths = 0
for cn, xr in recorded_values.items():
    sum_of_signal_strengths += cn * xr
print(f'The sum of the signal strengths is: {sum_of_signal_strengths}\n')

