import random
from labyrinth import Labyrinth, UserInputError


class PathGenerator:
    """Generates a randomized path from lower left corner to the upper right corner
    of a Labyrinth object.
    """

    def __init__(self, labyrinth: Labyrinth):
        """Saves the Labyrinth object on which the algorithm will make modifications.

        Args:
            labyrinth (Labyrinth):  The labyrinth on which the maze will be generated.
                                    Has to have at least one path cell
        """
        self.labyrinth = labyrinth
        self.random_manhattan_path = []

    def generate_random_shortest_path(self):
        """Generates a randomized path that is always heading towards the goal.
        The distance is always labyrinth.width + labyrinth.height - 1
        """
        self.random_manhattan_path = [(-1, 0)] * (self.labyrinth.height // 2)
        self.random_manhattan_path += [(0, 1)] * (self.labyrinth.width // 2)

        random.shuffle(self.random_manhattan_path)

        is_zigzag = self._check_if_path_is_zigzag()

        if is_zigzag:
            rand_index = random.randint(0, len(self.random_manhattan_path) - 2)
            (
                self.random_manhattan_path[rand_index],
                self.random_manhattan_path[rand_index + 1],
            ) = (
                self.random_manhattan_path[rand_index + 1],
                self.random_manhattan_path[rand_index],
            )

        self._write_manhattan_path_to_labyrinth()

        return self.labyrinth.labyrinth_matrix

    def _write_manhattan_path_to_labyrinth(self):
        """Writes the generated random manhattan path to the matrix
        of the Labyrinth object.
        """
        y = self.labyrinth.height - 1
        x = 0

        self.labyrinth.labyrinth_matrix[y][x] = "."
        for direction in self.random_manhattan_path:
            self.labyrinth.labyrinth_matrix[y + direction[0]][x + direction[1]] = "."
            self.labyrinth.broken_walls.append((y + direction[0], x + direction[1]))

            y += 2 * direction[0]
            x += 2 * direction[1]

            self.labyrinth.labyrinth_matrix[y][x] = "."

    def _check_if_path_is_zigzag(self):
        # If the path is a zigzag, as in it doesn't go in the same direction two times in a row,
        # then that means that no sidesteps can be generated.
        # Two steps in the same direction should be enough.
        # So if the path is a zigzag, then switch the positions of two adjacent indices.
        for i in range(0, len(self.random_manhattan_path) - 2):
            if self.random_manhattan_path[i] == self.random_manhattan_path[i + 1]:
                return False

        return True

    def generate_sidesteps(self):
        """Creates sidesteps to the randomly generated shortes path.
        Every sidesteps increases the path length by 4.
        """
        sidesteps_to_do = (
            self.labyrinth.steps_required
            - (self.labyrinth.width + self.labyrinth.height - 2)
        ) // 4

        while sidesteps_to_do > 0:
            if len(self.labyrinth.broken_walls) == 0:
                raise UserInputError(
                    """Labyrintin luonti epäonnistui, sillä vaadittavien askelten määrä on
                    liian iso. Kasvata labyrintin kokoa tai vähennä askelten määrää"""
                )
            # Choose a random wall from the list and remove it from the list.
            random_index = random.randint(0, len(self.labyrinth.broken_walls) - 1)
            (
                self.labyrinth.broken_walls[-1],
                self.labyrinth.broken_walls[random_index],
            ) = (
                self.labyrinth.broken_walls[random_index],
                self.labyrinth.broken_walls[-1],
            )

            current_broken_wall = self.labyrinth.broken_walls.pop()
            y = current_broken_wall[0]
            x = current_broken_wall[1]

            horizontal_sidestep = self._check_if_horizontal_sidestep_can_be_done(x, y)

            if horizontal_sidestep:
                directions = [(0, 2), (0, -2)]
            else:
                directions = [(2, 0), (-2, 0)]

            random.shuffle(directions)

            for direction in directions:
                if self._sidestep_can_be_generated_in_direction(
                    horizontal_sidestep, direction, x, y
                ):
                    self._add_sidestep_to_labyrinth_matrix(direction, x, y)
                    sidesteps_to_do -= 1

        return self.labyrinth.labyrinth_matrix

    def _check_if_horizontal_sidestep_can_be_done(self, x, y):
        try:
            if (
                self.labyrinth.labyrinth_matrix[y + 1][x] == "."
                and self.labyrinth.labyrinth_matrix[y - 1][x] == "."
                and y > 0
            ):
                return True
        except IndexError:
            pass

        return False

    def _sidestep_can_be_generated_in_direction(
        self, horizontal_sidestep: bool, direction: tuple, x: int, y: int
    ):
        try:
            if horizontal_sidestep:
                return bool(
                    self.labyrinth.labyrinth_matrix[y + 1][x + direction[1]] == "#"
                    and self.labyrinth.labyrinth_matrix[y - 1][x + direction[1]] == "#"
                    and y > 0
                    and x + direction[1] >= 0
                )

            return bool(
                self.labyrinth.labyrinth_matrix[y + direction[0]][x + 1] == "#"
                and self.labyrinth.labyrinth_matrix[y + direction[0]][x - 1] == "#"
                and x > 0
                and y + direction[0] >= 0
            )
        except IndexError:
            return False

    def _add_sidestep_to_labyrinth_matrix(self, direction: tuple, x: int, y: int):
        """Given a direction and a coordinate, writes the wanted sidestep into the labyrinth matrix

        Args:
            direction (tuple): The direction in which the sidestep should be generated.
            x (int): The x coordinate of the cell which the sidestep "should avoid".
            y (int): The y coordinate of the cell which the sidestep "should avoid".
        """

        horizontal_sidestep = bool(direction[0]==0)

        if horizontal_sidestep:
            self.labyrinth.labyrinth_matrix[y + 1][x + direction[1]] = "."
            self.labyrinth.labyrinth_matrix[y - 1][x + direction[1]] = "."
            self.labyrinth.labyrinth_matrix[y][x + direction[1]] = "."

            self.labyrinth.broken_walls.append((y, x + direction[1]))

            self.labyrinth.labyrinth_matrix[y + 1][x + (direction[1] // 2)] = "."
            self.labyrinth.labyrinth_matrix[y - 1][x + (direction[1] // 2)] = "."
            self.labyrinth.broken_walls.append((y + 1, x + (direction[1] // 2)))
            self.labyrinth.broken_walls.append((y - 1, x + (direction[1] // 2)))

            self.labyrinth.labyrinth_matrix[y][x] = "#"
            return

        if (
            self.labyrinth.labyrinth_matrix[y + direction[0]][x + 1] == "#"
            and self.labyrinth.labyrinth_matrix[y + direction[0]][x - 1] == "#"
            and x > 0
            and y + direction[0] >= 0
        ):
            self.labyrinth.labyrinth_matrix[y + direction[0]][x + 1] = "."
            self.labyrinth.labyrinth_matrix[y + direction[0]][x - 1] = "."
            self.labyrinth.labyrinth_matrix[y + direction[0]][x] = "."

            self.labyrinth.broken_walls.append((y + direction[0], x))

            self.labyrinth.labyrinth_matrix[y + (direction[0] // 2)][x + 1] = "."
            self.labyrinth.labyrinth_matrix[y + (direction[0] // 2)][x - 1] = "."
            self.labyrinth.broken_walls.append((y + (direction[0] // 2), x + 1))
            self.labyrinth.broken_walls.append((y + (direction[0] // 2), x - 1))

            self.labyrinth.labyrinth_matrix[y][x] = "#"

            return
