# adventOfCode 2022 day 02
# https://adventofcode.com/2022/day/02


from enum import Enum
class Plays(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def score_my_shape(first_column, second_column):
    op_choice = {'A': Plays.ROCK, 'B': Plays.PAPER, 'C': Plays.SCISSORS}[first_column]
    index_diff = {'X': -1, 'Y': 0, 'Z': 1}[second_column]
    my_choice = Plays((op_choice.value + index_diff) % 3)
    return {Plays.ROCK:1, Plays.PAPER:2, Plays.SCISSORS:3}[my_choice]

def score_game_outcome(second_column):
    return {'X': 0, 'Y': 3, 'Z': 6}[second_column]
    

my_total_score = 0
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        first_column, second_column = (x for i,x in enumerate(in_string) if i in [0,2])
        my_total_score += score_my_shape(first_column, second_column) + score_game_outcome(second_column)


print(f'The answer to B is {my_total_score}\n')

def test_score_my_shape():
    # Below are the given examples (all three had the player choose Rock, so one is the right-hand side value of all three)
    assert score_my_shape('A', 'Y') == 1
    assert score_my_shape('B', 'X') == 1
    assert score_my_shape('C', 'Z') == 1

def test_score_game_outcome():
    assert score_game_outcome('X') == 0
    assert score_game_outcome('Y') == 3
    assert score_game_outcome('Z') == 6



