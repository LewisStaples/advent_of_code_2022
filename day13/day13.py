# adventOfCode 20xy day 13
# https://adventofcode.com/20xy/day/13


from enum import Enum
class Inequality(Enum):
    CORRECTLY_ORDERED = 1
    INCORRECTLY_ORDERED = 2
    NOT_YET_DETERMINED = 3
    
def compare(left_ele, right_ele):
    if isinstance(left_ele, int) and isinstance(right_ele, int):
        if left_ele < right_ele:
            return Inequality.CORRECTLY_ORDERED
        elif left_ele > right_ele:
            return Inequality.INCORRECTLY_ORDERED
        else:
            return Inequality.NOT_YET_DETERMINED

    if isinstance(left_ele, int):
        left_ele = [left_ele]

    if isinstance(right_ele, int):
        right_ele = [right_ele]

    if isinstance(left_ele, list) and isinstance(right_ele, list):
        shortest_list_len = min(len(left_ele), len(right_ele))
        for the_index in range(shortest_list_len):
            ret_val = compare(left_ele[the_index], right_ele[the_index])
            if ret_val != Inequality.NOT_YET_DETERMINED:
                return ret_val
        if len(left_ele) < len(right_ele):
            return Inequality.CORRECTLY_ORDERED
        elif len(left_ele) > len(right_ele):
            return Inequality.INCORRECTLY_ORDERED
        else:
            return Inequality.NOT_YET_DETERMINED
        
def in_correct_order(left_packet_str, right_packet_str):
    left_packet = eval(left_packet_str)
    right_packet = eval(right_packet_str)
    while True:
        ret_val = compare(left_packet, right_packet)
        if ret_val == Inequality.CORRECTLY_ORDERED:
            return True
        elif ret_val == Inequality.INCORRECTLY_ORDERED:
            return False
        else:
            raise ValueError('incorrect_order returning invalid result!')
            

sum_total = 0

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        # print(in_string)

        if line_num % 3 == 0:
            left_packet_str = in_string
            continue
        elif line_num % 3 == 2:
            continue

        # implicit else (when line_num % 3 == 2)
        right_packet_str = in_string
        pair_number = line_num // 3 + 1
        # print(f'pair number: {pair_number}')
        if in_correct_order(left_packet_str, right_packet_str):
            # print("They are in the correct order")
            sum_total += pair_number
print(f'The sum is {sum_total}\n')


