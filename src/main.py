#!/usr/bin/env python
import copy

from labyrinth import Labyrinth, UserInputError
from labyrinth_drawer import LabyrinthDrawer
from generators.path_generator import PathGenerator
from generators.maze_generator_dfs import MazeGeneratorDFS
from generators.maze_generator_prim import MazeGeneratorPrim

def get_int_input(message : str):
    while True:
        # Test if the input is acceptable
        try:
            value = int(input(message))
            Labyrinth(value, value, 2*value + 6)
            return value
        except UserInputError as error:
            print(f"\n{error}\n")
        except ValueError:
            return None

if __name__ == "__main__":
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


        while True:
            try:
                required_steps = int(input("Syötä askelten määrä, jossa labyrintti täytyy läpäistä: "))
                labyrinth = Labyrinth(width, height, required_steps)
                break
            except UserInputError as error:
                print(f"\n{error}\n")
            except ValueError:
                labyrinth = None
                break
        
        if not labyrinth:
            break

        PathGenerator(labyrinth).generate_random_shortest_path()
        shortest_path = copy.deepcopy(labyrinth)

        PathGenerator(labyrinth).generate_sidesteps()
        path_with_sidesteps = copy.deepcopy(labyrinth)

        MazeGeneratorPrim(labyrinth).generate_maze_around_path()
        prim = labyrinth

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

        
