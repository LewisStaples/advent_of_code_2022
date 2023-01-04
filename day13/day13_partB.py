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
            raise ValueError("incorrect_order returning invalid result!")

# Using information from documentation about using sorted with
# a key function that is driven by a compare function
# https://wiki.python.org/moin/HowTo/Sorting/#The_Old_Way_Using_the_cmp_Parameter
def cmp_to_key(my_compare):
    "Convert a cmp= function into a key= function"

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return my_compare(self.obj, other.obj)

        def __gt__(self, other):
            return not my_compare(self.obj, other.obj)

        def __eq__(self, other):
            return False

        def __le__(self, other):
            return my_compare(self.obj, other.obj)

        def __ge__(self, other):
            return not my_compare(self.obj, other.obj)

        def __ne__(self, other):
            return True

    return K


orig_packets = list()
divider_packets = ["[[2]]", "[[6]]"]

orig_packets.extend(divider_packets)


# Reading input from the input file
input_filename = "input_sample0.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for line_num, in_string in enumerate(f):
        in_string = in_string.rstrip()
        if len(in_string) > 0:
            orig_packets.append(in_string)

sorted_packets = sorted(orig_packets, key=cmp_to_key(in_correct_order))

product_answer_B = 1
for packet in divider_packets:
    product_answer_B *= sorted_packets.index(packet) + 1

print(f"The solution to part B is {product_answer_B}\n")
