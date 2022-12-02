# adventOfCode 2022 day 02
# https://adventofcode.com/2022/day/02


from enum import Enum
class Plays(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def score_my_shape(my_choice):
    score_per_shape = {'X': 1, 'Y': 2, 'Z': 3}
    return score_per_shape[my_choice]

def score_game_outcome(op_choice_input, my_choice_input):
    op_choice_actual = {'A': Plays.ROCK, 'B': Plays.PAPER, 'C': Plays.SCISSORS}[op_choice_input]
    my_choice_actual = {'X': Plays.ROCK, 'Y': Plays.PAPER, 'Z': Plays.SCISSORS}[my_choice_input]
    
    if op_choice_actual.value == my_choice_actual.value:
        return 3
    if op_choice_actual.value - my_choice_actual.value in [1, -2]:
        return 0
    # in all other cases
    return 6

my_total_score = 0
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        op_choice, my_choice = (x for i,x in enumerate(in_string) if i in [0,2])
        my_total_score += score_my_shape(my_choice) + score_game_outcome(op_choice, my_choice)

print(f'The answer to A is {my_total_score}\n')

def test_score_my_shape():
    assert score_my_shape('X') == 1
    assert score_my_shape('Y') == 2
    assert score_my_shape('Z') == 3
