# adventOfCode 2022 day 21, Part B (part 2)
# https://adventofcode.com/2022/day/21

from dataclasses import dataclass
from sympy.solvers import solve
from sympy import Symbol


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
    monkeys["humn"].value = "humn"
    monkey_root_eq_components = monkeys["root"].equation.split(" ")
    monkeys["root"].equation = "".join(
        [monkey_root_eq_components[0], " == ", monkey_root_eq_components[2]]
    )
    return monkeys


def get_equation(monkeys, monkey_name):
    if monkeys[monkey_name].value == "humn":
        pass
    elif monkeys[monkey_name].value is None:
        rhs_terms = monkeys[monkey_name].equation.split(" ")
        l_value = get_equation(monkeys, rhs_terms[0])
        r_value = get_equation(monkeys, rhs_terms[2])
        eval_string = f"{l_value} {rhs_terms[1]} {r_value}"
        try:
            monkeys[monkey_name].value = int(eval(eval_string))
        except NameError:
            return " ( " + eval_string + " ) "
    return monkeys[monkey_name].value


def solve_equation(the_equation):
    the_expression = the_equation.replace("==", " ) - ( ")
    print("Solve for humn when the below expression equals zero:")
    print(f"{the_expression}\n")

    humn = Symbol("humn")
    return solve(the_expression, humn)


def solve_problem(input_filename):
    monkeys = get_input_data(input_filename)
    the_equation = get_equation(monkeys, "root")
    solved_variables = solve_equation(the_equation)

    print("The number that humn should yell for root to pass ")
    print(f"(the answer to part B) is:   {solved_variables[0]}\n")


solve_problem("input_sample0.txt")
