# adventOfCode 2022 day 01
# https://adventofcode.com/2022/day/01



def get_original_input(input_filename):
    original_input = []
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for input_line in f:
            input_line = input_line.rstrip()
            original_input.append(input_line)
    return original_input

def get_elves_calorie_totals(original_input):
    elves_calorie_totals = set()
    latest_calories = 0
    for line in original_input:
        if line.isdigit():
            latest_calories += int(line)
        else:
            elves_calorie_totals.add(latest_calories)
            latest_calories = 0
    return elves_calorie_totals

def solve_problem(input_filename):
    original_input = get_original_input(input_filename)
    elves_calorie_totals = get_elves_calorie_totals(original_input)
    print(f'The solution to part A is: {max(elves_calorie_totals)}\n')

    calories_top_three = 0
    sorted_list__elves_calorie_totals = sorted(list(elves_calorie_totals))
    for i in range(3):
        calories_top_three += sorted_list__elves_calorie_totals.pop()
    print(f'The solution to part B is: {calories_top_three}\n')

solve_problem('input.txt')

