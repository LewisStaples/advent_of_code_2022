# adventOfCode 2022 day 10
# https://adventofcode.com/2022/day/10


def do_recording_logic(recorded_values, cycle_number, x_register, pixels):
    # Part A recording logic
    if cycle_number in recorded_values:
        recorded_values[cycle_number] = x_register
    # Record the pixel (for part B)
    new_pixel = "."
    if (cycle_number - 1) % 40 in [x_register - 1, x_register, x_register + 1]:
        new_pixel = "#"
    if cycle_number % 40 == 1:
        pixels.append([])
    pixels[-1].append(new_pixel)


cycle_number = 1
x_register = 1
recorded_values = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}
pixels = []

input_filename = "input_sample1.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    for in_string in f:
        do_recording_logic(recorded_values, cycle_number, x_register, pixels)
        in_string = in_string.rstrip()
        if in_string[:4] == "addx":
            cycle_number += 1
            do_recording_logic(recorded_values, cycle_number, x_register, pixels)
            x_register += int(in_string[5:])
        cycle_number += 1

# Compute and display part A results
sum_of_signal_strengths = 0
for cn, xr in recorded_values.items():
    sum_of_signal_strengths += cn * xr
print(
    f"The sum of the signal strengths (part A results) is: {sum_of_signal_strengths}\n"
)

# Display part B results
print("Printing results for part B:")
for pixel_row in pixels:
    print("".join(pixel_row))
print()
