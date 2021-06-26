from .grid import Grid
import os


def ask_continue():
    print("continue? enter/n")
    user_input = input()
    return user_input


if __name__ == "__main__":
    os.system("cls")
    world = Grid(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    world.print_initial_state()
    user_input = ask_continue()

    while user_input != "n":
        os.system("cls")
        world.next_generation()
        print(world)
        user_input = ask_continue()
