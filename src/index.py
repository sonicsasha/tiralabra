import copy

from labyrinth import Labyrinth
from labyrinth_drawer import LabyrinthDrawer

if __name__ == "__main__":

    labyrinth = Labyrinth(1001, 501, 45824)
    labyrinth.generate_random_shortest_path()
    shortest_path = copy.deepcopy(labyrinth)

    labyrinth.generate_sidesteps()
    path_with_sidesteps = copy.deepcopy(labyrinth)

    labyrinth.generate_maze_around_path_prim()
    prim = labyrinth

    dfs = copy.deepcopy(path_with_sidesteps)
    dfs.generate_maze_around_path_dfs()

    LabyrinthDrawer(
        [
            (shortest_path, "Satunnainen lyhin polku"),
            (path_with_sidesteps, "Polku sivuaskelilla"),
            (prim, "Primin algoritmi"),
            (dfs, "Satunnainen syvyyshaku"),
        ]
    )
