from labyrinth import Labyrinth

if __name__ == "__main__":


    labyrinth = Labyrinth(51,51,188)
    labyrinth.generate_path_start_to_finish()
    labyrinth.generate_maze_around_path()
    labyrinth.draw_labyrinth()