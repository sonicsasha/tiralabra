import random


class UserInputError(Exception):
    """An exception that is raised when the user inputs an invalid value"""


class Labyrinth:
    """A class which generates a labyrinth, given a width, height and the steps required to complete
    the labyrinth.
    """

    def __init__(self, width: int, height: int, steps_required: int) -> None:
        """Checks if the inputs are correct, and if they are, generates an empty labyrinth of
        of given size.

        Args:
            width (int): The width of the labyrinth (has to be an odd number)
            height (int): The height of the labyrinth (has to be an odd number)
            steps_required (int): The amount of steps needed to complete the labyrinth.
            Has to satisfy the condition (steps_required - width - height + 2) mod 4 = 0.

        Raises:
            UserInputError: The user tries to create a 1x1 labyrinth
            UserInputError: The user tries to create a labyrinth with an even height or width
            UserInputError: The user tries to complete a labyrinth in a too small number of steps
            UserInputError: The user tries to complete a labyrinth in an amount of steps
                            that doesn't satisfy the condition of required steps.
        """
        min_step_count = width + height - 2
        if width == 1 and height == 1:
            raise UserInputError("Ei voida luoda 1x1 labyrinttiä")

        if width % 2 == 0 or height % 2 == 0:
            raise UserInputError(
                "Labyrintin leveyden ja korkeuden täytyy olla parittomia lukuja."
            )

        if min_step_count > steps_required:
            raise UserInputError(
                f"""Annetun kokoista labyrinttiä ei pysty ratkaisemaan
                    annetussa määrässä askelia.
                    Ole hyvä ja anna joko pienempi labyrintin koko tai suurempi määrä askelia.
                    Pienin määrä askelia annetuulla koolla on {min_step_count}"""
            )

        if (steps_required - min_step_count) % 4 != 0:
            acceptable_step_count = (
                min_step_count + ((steps_required - min_step_count) // 4) * 4
            )
            raise UserInputError(
                f"""Annetun kokoista labyrinttiä ei pysty ratkaisemaan
                annetussa määrässä askelia.
                Ole hyvä, ja anna joko eri labyrintin koko tai eri määrä askelia.
                Lähimmät mahdolliset askeleet ovat
                {acceptable_step_count} ja {acceptable_step_count + 4}"""
            )

        self.labyrinth_matrix = []
        self.width = width
        self.height = height
        self.steps_required = steps_required

        # This is used for the randomized path generation
        self.broken_walls = []

        # This is used for Prim's algorithm
        self.walls_to_break = []

        # If conditions are met and everything is alright, generate an empty maze filled with "#"

        for _ in range(0, height):
            self.labyrinth_matrix.append(["#"] * width)

    def generate_maze_dfs(self):
        """A function that generates a maze using the class' variables.
        The generated maze is created using randomized depth first algorithm.
        Used for tests.
        """
        self.generate_random_shortest_path()
        self.generate_sidesteps()
        self.generate_maze_around_path_dfs()

    def generate_maze_prim(self):
        """A function that generates a maze using the class' variables.
        The generated maze is created using randomized Prim's algorithm.
        Used for tests.
        """
        self.generate_random_shortest_path()
        self.generate_sidesteps()
        self.generate_maze_around_path_prim()

    def generate_random_shortest_path(self):
        """Generates a randomized path that is always heading towards the goal.
        The distance is always width + height - 1
        """
        path = []
        path += [(-1, 0)] * (self.height // 2)
        path += [(0, 1)] * (self.width // 2)

        random.shuffle(path)

        is_zigzag = True

        # If the path is a zigzag, as in it doesn't go in the same direction two times in a row,
        # then that means that no sidesteps can be generated.
        # Two steps in the same direction should be enough.
        # So if the path is a zigzag, then switch the positions of two adjacent indices.
        for i in range(0, len(path) - 2):
            if path[i] == path[i + 1]:
                is_zigzag = False
                break

        if is_zigzag:
            rand_index = random.randint(0, len(path) - 2)
            path[rand_index], path[rand_index + 1] = (
                path[rand_index + 1],
                path[rand_index],
            )

        y = self.height - 1
        x = 0

        self.labyrinth_matrix[y][x] = "."
        for direction in path:
            self.labyrinth_matrix[y + direction[0]][x + direction[1]] = "."
            self.broken_walls.append((y + direction[0], x + direction[1]))

            y += 2 * direction[0]
            x += 2 * direction[1]

            self.labyrinth_matrix[y][x] = "."

        return self.labyrinth_matrix

    def generate_sidesteps(self):
        """Creates sidesteps to the randomly generated shortes path.
        Every sidesteps increases the path length by 4.
        """
        sidesteps_to_do = (self.steps_required - (self.width + self.height - 2)) // 4

        while sidesteps_to_do > 0:
            if len(self.broken_walls) == 0:
                raise UserInputError(
                    """Labyrintin luonti epäonnistui, sillä vaadittavien askelten määrä on
                    liian iso. Kasvata labyrintin kokoa tai vähennä askelten määrää"""
                )
            # Choose a random wall from the list and remove it from the list.
            random_index = random.randint(0, len(self.broken_walls) - 1)
            self.broken_walls[-1], self.broken_walls[random_index] = (
                self.broken_walls[random_index],
                self.broken_walls[-1],
            )

            current_broken_wall = self.broken_walls.pop()
            y = current_broken_wall[0]
            x = current_broken_wall[1]

            horizontal_sidestep = False
            try:
                if (
                    self.labyrinth_matrix[y + 1][x] == "."
                    and self.labyrinth_matrix[y - 1][x] == "."
                    and y >= 0
                ):
                    horizontal_sidestep = True
            except IndexError:
                pass

            if horizontal_sidestep:
                directions = [(0, 2), (0, -2)]
            else:
                directions = [(2, 0), (-2, 0)]

            random.shuffle(directions)

            for direction in directions:
                try:
                    if horizontal_sidestep:
                        if (
                            self.labyrinth_matrix[y + 1][x + direction[1]] == "#"
                            and self.labyrinth_matrix[y - 1][x + direction[1]] == "#"
                            and y > 0
                            and x + direction[1] >= 0
                        ):
                            self.labyrinth_matrix[y + 1][x + direction[1]] = "."
                            self.labyrinth_matrix[y - 1][x + direction[1]] = "."
                            self.labyrinth_matrix[y][x + direction[1]] = "."

                            self.broken_walls.append((y, x + direction[1]))

                            self.labyrinth_matrix[y + 1][x + (direction[1] // 2)] = "."
                            self.labyrinth_matrix[y - 1][x + (direction[1] // 2)] = "."
                            self.broken_walls.append((y + 1, x + (direction[1] // 2)))
                            self.broken_walls.append((y - 1, x + (direction[1] // 2)))

                            self.labyrinth_matrix[y][x] = "#"

                            sidesteps_to_do -= 1
                            break

                    else:
                        if (
                            self.labyrinth_matrix[y + direction[0]][x + 1] == "#"
                            and self.labyrinth_matrix[y + direction[0]][x - 1] == "#"
                            and x > 0
                            and y + direction[0] >= 0
                        ):
                            self.labyrinth_matrix[y + direction[0]][x + 1] = "."
                            self.labyrinth_matrix[y + direction[0]][x - 1] = "."
                            self.labyrinth_matrix[y + direction[0]][x] = "."

                            self.broken_walls.append((y + direction[0], x))

                            self.labyrinth_matrix[y + (direction[0] // 2)][x + 1] = "."
                            self.labyrinth_matrix[y + (direction[0] // 2)][x - 1] = "."
                            self.broken_walls.append((y + (direction[0] // 2), x + 1))
                            self.broken_walls.append((y + (direction[0] // 2), x - 1))

                            self.labyrinth_matrix[y][x] = "#"

                            random.shuffle(self.broken_walls)
                            sidesteps_to_do -= 1
                            break
                except IndexError:
                    pass

        return self.labyrinth_matrix

    def generate_maze_around_path_dfs(self):
        """Given that a random path from start to finish has been generated,
        generate a maze around that path

        Returns:
            list: A matrix representing the labyrinth.
        """

        # Check the path which has been generated.
        # This will allow the program to randomly choose a cell
        # from which to start generating the maze.
        path_cells = []

        for row_number, row in enumerate(self.labyrinth_matrix):
            for column_number, cell in enumerate(row):
                if (
                    self.labyrinth_matrix[row_number][column_number] == "."
                    and row_number % 2 == 0
                    and column_number % 2 == 0
                    and not (row_number == 0 and column_number == self.width - 1)
                ):
                    path_cells.append((row_number, column_number))

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
                        self.labyrinth_matrix[cell[0] + direction[0]][
                            cell[1] + direction[1]
                        ]
                        == "#"
                    ):
                        self.labyrinth_matrix[cell[0] + direction[0] // 2][
                            cell[1] + direction[1] // 2
                        ] = "."
                        self.generate_random_path(
                            cell[0] + direction[0], cell[1] + direction[1]
                        )
                except IndexError:
                    pass

        return self.labyrinth_matrix

    def generate_random_path(self, y: int, x: int):
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
                self.labyrinth_matrix[new_cell[0]][new_cell[1]] == "#"
                and self.labyrinth_matrix[wall_break[0]][wall_break[1]] == "#"
            ):
                # Clear the currently selected cells.
                self.labyrinth_matrix[new_cell[0]][new_cell[1]] = "."
                self.labyrinth_matrix[wall_break[0]][wall_break[1]] = "."
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
                            self.labyrinth_matrix[new_cell[0] + direction[0]][
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

    def generate_maze_around_path_prim(self):
        """Given that a random path has been generated, creates a maze around that path
        using Prim's algorithm.

        The algorithm goes through every cell in the path
        and adds the adjacent walls and the cell those walls lead to to a list.
        """
        self.walls_to_break = []

        # Go through the path and add the walls of the path to a path list.

        for row_number, row in enumerate(self.labyrinth_matrix):
            for column_number, cell in enumerate(row):
                if (
                    self.labyrinth_matrix[row_number][column_number] == "."
                    and row_number % 2 == 0
                    and column_number % 2 == 0
                ):
                    self._add_adjacent_walls_to_list(row_number, column_number)

        while len(self.walls_to_break) > 0:
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
                self.labyrinth_matrix[wall_y][wall_x] == "#"
                and self.labyrinth_matrix[cell_y][cell_x] == "#"
            ):
                self.labyrinth_matrix[wall_y][wall_x] = "."
                self.labyrinth_matrix[cell_y][cell_x] = "."

                self._add_adjacent_walls_to_list(cell_y, cell_x)

        return self.labyrinth_matrix

    def _add_adjacent_walls_to_list(self, y, x):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            if y + direction[0] < 0 or x + direction[1] < 0:
                continue

            try:
                if (
                    self.labyrinth_matrix[y + direction[0]][x + direction[1]] == "#"
                    and self.labyrinth_matrix[y + 2 * direction[0]][
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
