#!/usr/bin/env python
import copy

from labyrinth import Labyrinth, UserInputError
from labyrinth_drawer import LabyrinthDrawer
from generators.path_generator import PathGenerator
from generators.maze_generator_dfs import MazeGeneratorDFS
from generators.maze_generator_prim import MazeGeneratorPrim

if __name__ == "__main__":
    print("Tervetuloa luomaan unelmiesi labyrintit!")
    print("Jätä syöte tyhjäksi poistuaksesi ohjelmasta")

    while True:

        try:
            print("")
            width = int(input("Syötä labyrintin leveys: "))
            height = int(input("Syötä labyrintin korkeus: "))
            required_steps = int(input("Syötä askelten määrä, jossa labyrintti täytyy läpäistä: "))

            labyrinth = Labyrinth(width, height, required_steps)
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
        except UserInputError as error:
            print(f"\n{error}\n")
        except ValueError:
            break
        
