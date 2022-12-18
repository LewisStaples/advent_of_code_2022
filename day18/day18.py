# adventOfCode 2022 day 18
# https://adventofcode.com/2022/day/18

from itertools import combinations


def get_vertices(input_filename):
    vertices = list()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            vertices.append(tuple([int(x) for x in in_string.split(",")]))
    return vertices


def get_manhattan_distance(vertex_pair):
    manhattan_distance = 0
    for i in range(len(vertex_pair[0])):
        manhattan_distance += abs(vertex_pair[0][i] - vertex_pair[1][i])
    return manhattan_distance


def get_num_edges_len_one(vertices):
    num_edges_len_one = 0
    for vertex_pair in combinations(vertices, 2):
        if get_manhattan_distance(vertex_pair) == 1:
            num_edges_len_one += 1
    return num_edges_len_one


def get_answer_part_a(num_edges_len_one, vertex_count):
    return 6 * vertex_count - 2 * num_edges_len_one


def solve_problem(input_filename):
    vertices = get_vertices(input_filename)
    if len(vertices) < 20:
        print(vertices)
        print()
    num_edges_len_one = get_num_edges_len_one(vertices)
    print(f"Answer to part A: {get_answer_part_a(num_edges_len_one, len(vertices))}\n")


solve_problem("input_sample1.txt")


def test_get_vertices():
    assert get_vertices("input_sample0.txt") == [(1, 1, 1), (2, 1, 1)]


def test_get_manhattan_distance():
    assert get_manhattan_distance([(1, 1, 1), (2, 1, 1)]) == 1


def test_get_num_edges_len_one():
    assert get_num_edges_len_one([(1, 1, 1), (2, 1, 1)]) == 1


def test_get_answer_part_a():
    assert get_answer_part_a(1, 2) == 10
