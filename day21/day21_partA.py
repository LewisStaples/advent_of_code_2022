# adventOfCode 2022 day 21
# https://adventofcode.com/2022/day/21

from dataclasses import dataclass


@dataclass
class Monkey:
    name: str
    value: int
    equation: str  # equation or string

    def __init__(self, name):
        self.name = name
        self.value = None


def get_input_data(input_filename):
    monkeys = dict()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            lhs, rhs = in_string.rstrip().split(": ")
            if lhs not in monkeys:
                monkeys[lhs] = Monkey(lhs)
            if " " in rhs:
                monkeys[lhs].equation = rhs
                rhs_components = rhs.split(" ")
                # remove operator (assumes there's only one binary operator)
                rhs_components.pop(1)
            else:
                monkeys[lhs].value = int(rhs)
    return monkeys


def get_value(monkeys, monkey_name):
    if monkeys[monkey_name].value is None:
        rhs_terms = monkeys[monkey_name].equation.split(" ")
        l_value = get_value(monkeys, rhs_terms[0])
        r_value = get_value(monkeys, rhs_terms[2])
        monkeys[monkey_name].value = eval(f"{l_value} {rhs_terms[1]} {r_value}")
    return monkeys[monkey_name].value


def solve_problem(input_filename):
    monkeys = get_input_data(input_filename)
    print(f'The answer to A is: {get_value(monkeys, "root")}')


solve_problem("input.txt")
