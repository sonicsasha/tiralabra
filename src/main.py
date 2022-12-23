import copy
import os

from labyrinth import Labyrinth, UserInputError
from labyrinth_drawer import LabyrinthDrawer
from generators.path_generator import PathGenerator
from generators.maze_generator_dfs import MazeGeneratorDFS
from generators.maze_generator_prim import MazeGeneratorPrim


def get_int_input(message: str) -> int:
    """Gets an input and turns it into an integer

    Args:
        message (str): The message to show to the player when getting the input

    Returns:
        int: Returns the number that the user inputted. None if not a number
    """
    while True:
        # Test if the input is acceptable
        try:
            value = int(input(message))
            Labyrinth(value, value, 2 * value + 6)
            return value
        except UserInputError as error_message:
            print(f"\n{error_message}\n")
        except ValueError:
            return None


if __name__ == "__main__":
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "true"
    print("Tervetuloa luomaan unelmiesi labyrintit!")
    print("Jätä syöte tyhjäksi poistuaksesi ohjelmasta")

    while True:
        print("")
        width = get_int_input("Syötä labyrintin leveys: ")
        if not width:
            break
        height = get_int_input("Syötä labyrintin korkeus: ")
        if not height:
            break

        required_steps = get_int_input("Syötä askelten määrä, jossa labyrintti täytyy läpäistä: ")
        if not required_steps:
            break

        while True:
            try:
                required_steps = int(
                    input("Syötä askelten määrä, jossa labyrintti täytyy läpäistä: ")
                )
                LABYRINTH = Labyrinth(width, height, required_steps)
                break
            except UserInputError as error:
                print(f"\n{error}\n")
            except ValueError:
                LABYRINTH = None
                break

        if not LABYRINTH:
            break

        PathGenerator(LABYRINTH).generate_random_shortest_path()
        shortest_path = copy.deepcopy(LABYRINTH)

        PathGenerator(LABYRINTH).generate_sidesteps()
        path_with_sidesteps = copy.deepcopy(LABYRINTH)

        MazeGeneratorPrim(LABYRINTH).generate_maze_around_path()
        prim = LABYRINTH

        dfs = copy.deepcopy(path_with_sidesteps)
        MazeGeneratorDFS(dfs).generate_maze_around_path()

        LabyrinthDrawer(
            [
                (shortest_path, "Satunnainen lyhin polku"),
                (path_with_sidesteps, "Polku sivuaskelilla"),
                (prim, "Primin algoritmi"),
                (dfs, "Satunnainen syvyyshaku"),
            ]
        )
