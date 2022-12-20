# adventOfCode 2022 day 18
# https://adventofcode.com/2022/day/18

from itertools import combinations
from enum import Enum


class PointType(Enum):
    VERTEX = (1,)
    EXTERNAL_VOID = (2,)
    INTERNAL_VOID = 3


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


def get_outer_bounding_box(vertices):
    outer_bounding_box = [
        [float("inf"), float("-inf")],
        [float("inf"), float("-inf")],
        [float("inf"), float("-inf")],
    ]
    for vertex in vertices:
        for i, coordinate in enumerate(vertex):
            if coordinate < outer_bounding_box[i][0]:
                outer_bounding_box[i][0] = coordinate
            if coordinate > outer_bounding_box[i][1]:
                outer_bounding_box[i][1] = coordinate
    return outer_bounding_box


def flood_fill(this_point, all_points_in_outer_bounding_box):
    next_flood_points = {this_point}
    already_flooded_points = set()  # list()
    already_checked_nonflooded_points = set()  # list()
    flag_label = PointType.INTERNAL_VOID
    while len(next_flood_points) > 0:
        next_point = next_flood_points.pop()
        # if next_point not in all_points_in_outer_bounding_box:
        #     continue
        if all_points_in_outer_bounding_box[next_point] is None:
            for direction in [
                (-1, 0, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]:
                next_flood_point = (
                    next_point[0] + direction[0],
                    next_point[1] + direction[1],
                    next_point[2] + direction[2],
                )
                # if all_points_in_outer_bounding_box[next_flood_point] is None:
                if next_flood_point not in already_flooded_points:
                    # if all_points_in_outer_bounding_box[next_flood_point] is None:
                    if next_flood_point not in already_checked_nonflooded_points:
                        next_flood_points.add(next_flood_point)
            already_flooded_points.add(next_point)
        elif all_points_in_outer_bounding_box[next_point] == PointType.EXTERNAL_VOID:
            flag_label = PointType.EXTERNAL_VOID
            already_checked_nonflooded_points.add(next_point)
        else:
            already_checked_nonflooded_points.add(next_point)
    for point in already_flooded_points:
        all_points_in_outer_bounding_box[point] = flag_label


def get_internal_non_vertices(outer_bounding_box, vertices):
    # For all points in bounding box, determine if they're
    # a vertex, an external non-vertex, or an internal non-vertex
    all_points_in_outer_bounding_box = dict()

    # Create a layer of PointType.EXTERNAL_VOID in points immediately
    # outside the bounding box
    # (points inside the bounding box will be temporarily set this way, too)
    for x in range(outer_bounding_box[0][0] - 1, outer_bounding_box[0][1] + 2):
        for y in range(outer_bounding_box[1][0] - 1, outer_bounding_box[1][1] + 2):
            for z in range(outer_bounding_box[2][0] - 1, outer_bounding_box[2][1] + 2):
                all_points_in_outer_bounding_box[(x, y, z)] = PointType.EXTERNAL_VOID

    # Set points to None inside the bounding box
    for x in range(outer_bounding_box[0][0], outer_bounding_box[0][1] + 1):
        for y in range(outer_bounding_box[1][0], outer_bounding_box[1][1] + 1):
            for z in range(outer_bounding_box[2][0], outer_bounding_box[2][1] + 1):
                all_points_in_outer_bounding_box[(x, y, z)] = None

    # Label all vertices
    for vertex in vertices:
        all_points_in_outer_bounding_box[vertex] = PointType.VERTEX

    for this_point in all_points_in_outer_bounding_box:
        if all_points_in_outer_bounding_box[this_point] is None:
            flood_fill(this_point, all_points_in_outer_bounding_box)

    internal_non_vertices = []
    for k, v in all_points_in_outer_bounding_box.items():
        if v == PointType.INTERNAL_VOID:
            internal_non_vertices.append(k)

    return internal_non_vertices


def get_count_edges_internal_to_vertex(vertices, internal_non_vertices):
    count_edges_internal_to_vertex = 0
    for vertex in vertices:
        for internal_point in internal_non_vertices:
            if get_manhattan_distance((vertex, internal_point)) == 1:
                count_edges_internal_to_vertex += 1
    return count_edges_internal_to_vertex


def solve_problem(input_filename):
    # Input data
    vertices = get_vertices(input_filename)
    if len(vertices) < 20:
        print(vertices)
        print()

    # Steps to solve part A
    num_edges_len_one = get_num_edges_len_one(vertices)
    ans_A = get_answer_part_a(num_edges_len_one, len(vertices))
    print(f"Answer to part A: {ans_A}\n")

    # Steps to solve part B
    outer_bounding_box = get_outer_bounding_box(vertices)
    print(f"Outer Bounding Box: {outer_bounding_box}\n")
    internal_non_vertices = get_internal_non_vertices(outer_bounding_box, vertices)
    count_edges_internal_to_vertex = get_count_edges_internal_to_vertex(
        vertices, internal_non_vertices
    )
    ans_B = ans_A - count_edges_internal_to_vertex
    print(f"Answer to part B: {ans_B}\n")


solve_problem("input.txt")


def test_get_vertices():
    assert get_vertices("input_sample0.txt") == [(1, 1, 1), (2, 1, 1)]


def test_get_manhattan_distance():
    assert get_manhattan_distance([(1, 1, 1), (2, 1, 1)]) == 1


def test_get_num_edges_len_one():
    assert get_num_edges_len_one([(1, 1, 1), (2, 1, 1)]) == 1


def test_get_answer_part_a():
    assert get_answer_part_a(1, 2) == 10


def test_get_outer_bounding_box():
    assert get_outer_bounding_box([(1, 1, 1), (9, 3, 1), (-4, 8, 7)]) == [
        [-4, 9],
        [1, 8],
        [1, 7],
    ]
