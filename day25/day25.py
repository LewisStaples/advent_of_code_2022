# adventOfCode 2022 day 25
# https://adventofcode.com/2022/day/25


def get_decimal_value(snafu_str):
    decimal_value = 0
    for str_index, ch in enumerate(snafu_str):
        digit_value = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[snafu_str[str_index]]
        decimal_value += digit_value * 5 ** (len(snafu_str) - str_index - 1)
    return decimal_value


def calc_num_snafu_digits(decimal_value):
    status = {"num_digits": 1, "upper_limit": 2}
    while status["upper_limit"] < decimal_value:
        status["num_digits"] += 1
        status["upper_limit"] += 2 * 5 ** (status["num_digits"] - 1)
    return status["num_digits"]


def calc_nth_digit(remainder, num_snafu_digits, digit_num):
    for nth_digit in ["2", "1", "0", "-", "="]:
        smallest_snafu_with_this_nth_digit = nth_digit + "=" * (
            num_snafu_digits - digit_num - 1
        )
        if remainder >= get_decimal_value(smallest_snafu_with_this_nth_digit):
            remainder -= get_decimal_value(
                nth_digit + "0" * (num_snafu_digits - digit_num - 1)
            )
            break
    return nth_digit, remainder


def get_snafu_str(decimal_value):
    num_snafu_digits = calc_num_snafu_digits(decimal_value)
    remainder = decimal_value
    snafu_str = ""
    for digit_num in range(num_snafu_digits):
        nth_digit, remainder = calc_nth_digit(remainder, num_snafu_digits, digit_num)
        snafu_str += nth_digit

    return snafu_str


def get_input_lines(input_filename):
    input_list = []
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            input_list.append(in_string)
    return input_list


def get_decimal_list_from_snafu_list(input_snafu_str_list):
    decimal_list = []
    for snafu_str in input_snafu_str_list:
        decimal_list.append(get_decimal_value(snafu_str))
    return decimal_list


def solve_problem(input_filename):
    input_snafu_str_list = get_input_lines(input_filename)
    decimal_value_list = get_decimal_list_from_snafu_list(input_snafu_str_list)
    print(f"The total in decimal is {sum(decimal_value_list)}\n")
    print("The snafu string to use is: ", end="")
    print(get_snafu_str(sum(decimal_value_list)))
    print()


solve_problem("input_sample0.txt")
