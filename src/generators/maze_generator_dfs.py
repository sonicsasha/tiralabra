import random
from labyrinth import Labyrinth


class MazeGeneratorDFS:
    """Class that generates a maze using the randomized depth first search
    algorithm when given an object of class Labyrinth
    """

    def __init__(self, labyrinth: Labyrinth):
        """Saves the Labyrinth object on which the algorithm will make the modifications.

        Args:
            labyrinth (Labyrinth):  The labyrinth on which the maze will be generated.
                                    Has to have at least one path cell.
        """
        self.labyrinth = labyrinth

    def generate_maze_around_path(self):
        """Given that a random path from start to finish has been generated,
        generate a maze around that path

        Returns:
            list: A matrix representing the labyrinth.
        """

        # Check the path which has been generated.
        # This will allow the program to randomly choose a cell
        # from which to start generating the maze.

        path_cells = self._find_path_cells()

        # Go through every cell in the path so that there is a path in every area of the maze.

        random.shuffle(path_cells)

        directions = [(-2, 0), (2, 0), (0, 2), (0, -2)]

        for cell in path_cells:
            random.shuffle(directions)

            # Try to start a depth search in every direction until it can be started.
            for direction in directions:
                try:
                    if cell[0] + direction[0] < 0 or cell[1] + direction[1] < 0:
                        continue

                    if (
                        self.labyrinth.labyrinth_matrix[cell[0] + direction[0]][
                            cell[1] + direction[1]
                        ]
                        == "#"
                    ):
                        self.labyrinth.labyrinth_matrix[cell[0] + direction[0] // 2][
                            cell[1] + direction[1] // 2
                        ] = "."
                        self._generate_random_path(
                            cell[0] + direction[0], cell[1] + direction[1]
                        )
                except IndexError:
                    pass

        return self.labyrinth.labyrinth_matrix

    def _find_path_cells(self):
        path_cells = []

        for row_number, row in enumerate(self.labyrinth.labyrinth_matrix):
            for column_number, cell in enumerate(row):
                if (
                    cell == "."
                    and row_number % 2 == 0
                    and column_number % 2 == 0
                    and not (
                        row_number == 0 and column_number == self.labyrinth.width - 1
                    )
                ):
                    path_cells.append((row_number, column_number))

        return path_cells

    def _generate_random_path(self, y: int, x: int):
        """Given a cell, start a randomized depth search from said cell
        and generate a maze from said cell

        Args:
            y (int): The y coordinate of the cell from which the depth search will start.
            x (int): The x coordinate of the cell from which the depth search will start.
        """
        stack = []
        # Whenever we move in a certain direction in a maze, we have to move two steps.
        # That's why we add a tuple consisting of two tuples to the stack.
        stack.append(((y, x), (y, x)))
        directions = [(-2, 0), (2, 0), (0, 2), (0, -2)]
        while len(stack) != 0:
            current = stack.pop()
            wall_break = current[0]
            new_cell = current[1]
            if (
                self.labyrinth.labyrinth_matrix[new_cell[0]][new_cell[1]] == "#"
                and self.labyrinth.labyrinth_matrix[wall_break[0]][wall_break[1]] == "#"
            ):
                # Clear the currently selected cells.
                self.labyrinth.labyrinth_matrix[new_cell[0]][new_cell[1]] = "."
                self.labyrinth.labyrinth_matrix[wall_break[0]][wall_break[1]] = "."
                random.shuffle(directions)
                # Add all the directions we can move in to the stack.
                for direction in directions:
                    try:
                        if (
                            new_cell[0] + direction[0] < 0
                            or new_cell[1] + direction[1] < 0
                        ):
                            continue

                        if (
                            self.labyrinth.labyrinth_matrix[new_cell[0] + direction[0]][
                                new_cell[1] + direction[1]
                            ]
                            == "#"
                        ):
                            stack.append(
                                (
                                    (
                                        new_cell[0] + direction[0] // 2,
                                        new_cell[1] + direction[1] // 2,
                                    ),
                                    (
                                        new_cell[0] + direction[0],
                                        new_cell[1] + direction[1],
                                    ),
                                )
                            )

                    except IndexError:
                        pass
