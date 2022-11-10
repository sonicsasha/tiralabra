from labyrinth import Labyrinth
from labyrinth_drawer import draw_labyrinth

if __name__ == "__main__":

    labyrinth = Labyrinth(1001, 1001, 2800)
    labyrinth.generate_random_shortest_path()
    labyrinth.generate_sidesteps()
    labyrinth.generate_maze_around_path()

    draw_labyrinth(labyrinth)
