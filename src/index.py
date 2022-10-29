from labyrinth import Labyrinth

if __name__ == "__main__":
    labyrinth = Labyrinth(5,3,10)
    labyrinth.set_labyrinth (["#.#.",
                            "..#.",
                            "#...",
                            "..##"])
    labyrinth.draw_labyrinth()