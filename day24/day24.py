#!/usr/bin/env python3

# adventOfCode 2022 day 24
# https://adventofcode.com/2022/day/24


direction = {
    "^": {"vector": -1j},
    "v": {"vector": 1j},
    "<": {"vector": -1},
    ">": {"vector": 1},
}


def get_initial_state(input_filename):
    initial_state = {
        "walls": set(),
        "initial_blizzards_locations": list(),
        "initial_blizzards_directions": list(),
        "entrance": None,
        "exit": None,
    }
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    print("Displaying original input:")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_num, in_string in enumerate(f):
            in_list = list(in_string.rstrip())
            for col_num, ch in enumerate(in_list):
                if ch == "#":
                    initial_state["walls"].add(col_num - 1 + 1j * (line_num - 1))
                if ch in direction:
                    initial_state["initial_blizzards_locations"].append(
                        col_num - 1 + (line_num - 1) * 1j
                    )
                    initial_state["initial_blizzards_directions"].append(
                        direction[ch]["vector"]
                    )
            if line_num == 0:
                initial_state["entrance"] = in_list.index(".") - 1 + (line_num - 1) * 1j
                # The below wall char prevents the expedition from
                # exiting the valley via the entrance site
                initial_state["walls"].add(in_list.index(".") - 1 + -2j)
            print(in_string.rstrip())
    print()
    initial_state["exit"] = in_list.index(".") - 1 + (line_num - 1) * 1j
    initial_state["minute_counter"] = 0
    initial_state["poss_curr_expedition_locns"] = {initial_state["entrance"]}
    initial_state["valley_dimensions"] = len(in_list) - 2 + (line_num + 1 - 2) * 1j
    return initial_state


def get_current_blizzards_state(state):
    current_blizzards_state = set()
    for the_index in range(len(state["initial_blizzards_locations"])):
        blizzard_location = (
            state["initial_blizzards_locations"][the_index]
            + state["initial_blizzards_directions"][the_index] * state["minute_counter"]
        )
        blizzard_location = (
            blizzard_location.real % state["valley_dimensions"].real
            + blizzard_location.imag % state["valley_dimensions"].imag * 1j
        )
        current_blizzards_state.add(blizzard_location)
    return current_blizzards_state


def advance_one_minute(state, goal):
    state["minute_counter"] += 1
    # Get current blizzard state
    current_blizzards_state = get_current_blizzards_state(state)
    # update expedition list of possible states
    new_poss_curr_expedition_locns = set()
    for curr_locn in state["poss_curr_expedition_locns"]:
        new_pot_locns = {curr_locn}
        for dir_grp in direction.values():
            new_pot_locns.add(curr_locn + dir_grp["vector"])
        for new_pot_locn in new_pot_locns:
            # If this location has already been identified as a good one, skip it
            if new_pot_locn in new_poss_curr_expedition_locns:
                continue
            # If it's a wall, skip it
            if new_pot_locn in state["walls"]:
                continue
            # If goal ... finished
            if new_pot_locn == state[goal]:
                state["poss_curr_expedition_locns"] = {state[goal]}
                return state["minute_counter"]
            # # If blizzard, skip it
            if new_pot_locn in current_blizzards_state:
                continue
            # It's a good location, so add it to the list of new locations
            new_poss_curr_expedition_locns.add(new_pot_locn)

    # The goal has not yet been reached
    state["poss_curr_expedition_locns"] = new_poss_curr_expedition_locns
    return None


def display(state):
    # Display timestamp
    print(f"Valley at minute {state['minute_counter']}")

    if len(state["walls"]) > 50:
        return

    # Loop through coordinates
    for b in range(-1, int(state["valley_dimensions"].imag + 1)):
        for a in range(-1, int(state["valley_dimensions"].real + 1)):
            position = a + (1j * b)
            # Display wall
            if position in state["walls"]:
                print("#", end="")
                continue

            # Display blizzard ('B' will be shown for all blizzards,
            # no matter what direction the blizzard is moving in)
            if position in get_current_blizzards_state(state):
                print("B", end="")
                continue

            # Display entrance
            if position == state["entrance"]:
                print("N", end="")
                continue

            # Display exit
            if position == state["exit"]:
                print("X", end="")
                continue

            # Display empty space
            print(".", end="")
        print()
    print()


def get_minutes_to_goal(state, goal):
    display(state)

    while True:
        aom = advance_one_minute(state, goal)
        if aom is not None:
            display(state)
            return aom

        display(state)


def solve_problem(input_filename):
    state = get_initial_state(input_filename)
    minutes_to_goal_one = get_minutes_to_goal(state, "exit")
    get_minutes_to_goal(state, "entrance")
    minutes_to_goal_last = get_minutes_to_goal(state, "exit")

    print(f"Part A answer: it takes {minutes_to_goal_one} min. to reach the first exit")
    print(f"Part B answer: it takes {minutes_to_goal_last} min. to reach the last exit")
    print(f"Again, these results were based on input from {input_filename}\n")


solve_problem("input_sample1.txt")
