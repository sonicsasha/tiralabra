import copy
import os

from labyrinth import Labyrinth
from labyrinth_drawer import LabyrinthDrawer
from generators.path_generator import PathGenerator
from generators.maze_generator_dfs import MazeGeneratorDFS
from generators.maze_generator_prim import MazeGeneratorPrim

if __name__ == "__main__":
    labyrinth = Labyrinth(1001, 501, 45824)
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
