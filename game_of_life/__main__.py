from typing import Tuple
from .grid import Grid
import os


def ask_continue():
    print("continue? enter/n")
    user_input = input()
    return user_input


def get_lines_cols_from_input() -> Tuple[int, int]:

    print("Enter board size (Lines Columns):")
    input_size = input()

    while len(input_size.split(" ")) != 2:
        print("invalid input size, try again, example : '10 15'")
        input_size = input()

    input_array = list(map(int, input_size.split(" ")))
    os.system("cls")

    return input_array[0], input_array[1]


if __name__ == "__main__":
    os.system("cls")

    n_lines, n_cols = get_lines_cols_from_input()
    world = Grid.from_random_start(n_lines=n_lines, n_columns=n_cols)

    print(world)
    user_input = ask_continue()

    while user_input != "n":
        os.system("cls")
        world.next_generation()
        print(world)
        print(f"Generation #{world.n_generation}")
        user_input = ask_continue()
