# adventOfCode 2022 day 11
# https://adventofcode.com/2022/day/11


class Monkey:
    def __init__(self):
        pass

    def add_worry_levels(self, worry_list_input):
        self.worry_levels = [int(x) for x in worry_list_input.split(", ")]

    def add_operation(self, operation_input):
        self.operation_input = operation_input

    def add_divisional_test(self, divisional_test_input):
        self.divisional_test = int(divisional_test_input)

    def add_true_monkey_number(self, true_monkey_number):
        self.true_monkey_number = int(true_monkey_number)

    def add_false_monkey_number(self, false_monkey_number):
        self.false_monkey_number = int(false_monkey_number)


monkeys_attributes = []
lcm = 1

# Reading input from the input file
input_filename = "input.txt"
print(f"\nUsing input file: {input_filename}\n")
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if in_string[:7] == "Monkey ":
            if len(monkeys_attributes) != int(in_string[7:-1]):
                raise ValueError("Bad index of Monkey in input file")
            monkeys_attributes.append(Monkey())
        elif in_string[:18] == "  Starting items: ":
            monkeys_attributes[-1].add_worry_levels(in_string[18:])
        elif in_string[:19] == "  Operation: new = ":
            monkeys_attributes[-1].add_operation(in_string[19:])
        elif in_string[:21] == "  Test: divisible by ":
            monkeys_attributes[-1].add_divisional_test(in_string[21:])
            lcm *= int(in_string[21:])
        elif in_string[:29] == "    If true: throw to monkey ":
            monkeys_attributes[-1].add_true_monkey_number(in_string[29:])
        elif in_string[:30] == "    If false: throw to monkey ":
            monkeys_attributes[-1].add_false_monkey_number(in_string[30:])

monkey_id = 0
round_number = 1
monkey_inspection_counts = {
    monkey_id: 0 for monkey_id in range(len(monkeys_attributes))
}
while True:
    while len(monkeys_attributes[monkey_id].worry_levels) > 0:
        monkey_inspection_counts[monkey_id] += 1
        old = monkeys_attributes[monkey_id].worry_levels.pop(0)
        worry_level = eval(monkeys_attributes[monkey_id].operation_input)
        worry_level %= lcm
        if worry_level % monkeys_attributes[monkey_id].divisional_test == 0:
            monkeys_attributes[
                monkeys_attributes[monkey_id].true_monkey_number
            ].worry_levels.append(worry_level)
        else:
            monkeys_attributes[
                monkeys_attributes[monkey_id].false_monkey_number
            ].worry_levels.append(worry_level)
    monkey_id = (monkey_id + 1) % len(monkeys_attributes)
    if monkey_id == 0:
        round_number += 1
    if round_number > 10000:
        break

# inspec_cts is defined to be inspection_counts, sorted in descending order
inspec_cts = sorted(list(monkey_inspection_counts.values()), reverse=True)
print(f"The answer to part B is {inspec_cts[0] * inspec_cts[1]}\n")
