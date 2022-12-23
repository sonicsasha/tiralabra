import random
from labyrinth import Labyrinth


class MazeGeneratorPrim:
    """Class that generates a maze using the randomized Prim's algorithm
    when given an object of class Labyrinth
    """

    def __init__(self, labyrinth: Labyrinth):
        """Saves the Labyrinth object on which the algorithm will make the modifications.

        Args:
            labyrinth (Labyrinth):  The labyrinth on which the maze will be generated.
                                    Has to have at least one path cell.
        """
        self.labyrinth = labyrinth
        self.walls_to_break = []

    def generate_maze_around_path(self):
        """Given that a random path has been generated, creates a maze around that path
        using Prim's algorithm.

        The algorithm goes through every cell in the path
        and adds the adjacent walls and the cell those walls lead to to a list.
        """

        # Go through the path and add the walls of the path to a path list.

        self._find_walls_to_break()

        while len(self.walls_to_break) > 0:
            self._break_random_wall()

        return self.labyrinth.labyrinth_matrix

    def _find_walls_to_break(self):
        for row_number, row in enumerate(self.labyrinth.labyrinth_matrix):
            for column_number, cell in enumerate(row):
                if cell == "." and row_number % 2 == 0 and column_number % 2 == 0:
                    self._add_adjacent_walls_to_list(row_number, column_number)

    def _break_random_wall(self):
        # Pop a random item from list
        i = random.randrange(len(self.walls_to_break))
        self.walls_to_break[i], self.walls_to_break[-1] = (
            self.walls_to_break[-1],
            self.walls_to_break[i],
        )
        wall, cell = self.walls_to_break.pop()

        wall_y = wall[0]
        wall_x = wall[1]

        cell_y = cell[0]
        cell_x = cell[1]

        if (
            self.labyrinth.labyrinth_matrix[wall_y][wall_x] == "#"
            and self.labyrinth.labyrinth_matrix[cell_y][cell_x] == "#"
        ):
            self.labyrinth.labyrinth_matrix[wall_y][wall_x] = "."
            self.labyrinth.labyrinth_matrix[cell_y][cell_x] = "."

            self._add_adjacent_walls_to_list(cell_y, cell_x)

    def _add_adjacent_walls_to_list(self, y, x):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            if y + direction[0] < 0 or x + direction[1] < 0:
                continue

            try:
                if (
                    self.labyrinth.labyrinth_matrix[y + direction[0]][x + direction[1]]
                    == "#"
                    and self.labyrinth.labyrinth_matrix[y + 2 * direction[0]][
                        x + 2 * direction[1]
                    ]
                    == "#"
                ):
                    self.walls_to_break.append(
                        (
                            (
                                y + direction[0],
                                x + direction[1],
                            ),
                            (
                                y + 2 * direction[0],
                                x + 2 * direction[1],
                            ),
                        )
                    )
            except IndexError:
                pass
