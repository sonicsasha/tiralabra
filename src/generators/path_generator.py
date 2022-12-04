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

    def generate_random_shortest_path(self):
        """Generates a randomized path that is always heading towards the goal.
        The distance is always labyrinth.width + labyrinth.height - 1
        """
        path = []
        path += [(-1, 0)] * (self.labyrinth.height // 2)
        path += [(0, 1)] * (self.labyrinth.width // 2)

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

        y = self.labyrinth.height - 1
        x = 0

        self.labyrinth.labyrinth_matrix[y][x] = "."
        for direction in path:
            self.labyrinth.labyrinth_matrix[y + direction[0]][x + direction[1]] = "."
            self.labyrinth.broken_walls.append((y + direction[0], x + direction[1]))

            y += 2 * direction[0]
            x += 2 * direction[1]

            self.labyrinth.labyrinth_matrix[y][x] = "."

        return self.labyrinth.labyrinth_matrix

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

            horizontal_sidestep = False
            try:
                if (
                    self.labyrinth.labyrinth_matrix[y + 1][x] == "."
                    and self.labyrinth.labyrinth_matrix[y - 1][x] == "."
                    and y > 0
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
                            self.labyrinth.labyrinth_matrix[y + 1][x + direction[1]]
                            == "#"
                            and self.labyrinth.labyrinth_matrix[y - 1][x + direction[1]]
                            == "#"
                            and y > 0
                            and x + direction[1] >= 0
                        ):
                            self.labyrinth.labyrinth_matrix[y + 1][
                                x + direction[1]
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y - 1][
                                x + direction[1]
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y][x + direction[1]] = "."

                            self.labyrinth.broken_walls.append((y, x + direction[1]))

                            self.labyrinth.labyrinth_matrix[y + 1][
                                x + (direction[1] // 2)
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y - 1][
                                x + (direction[1] // 2)
                            ] = "."
                            self.labyrinth.broken_walls.append(
                                (y + 1, x + (direction[1] // 2))
                            )
                            self.labyrinth.broken_walls.append(
                                (y - 1, x + (direction[1] // 2))
                            )

                            self.labyrinth.labyrinth_matrix[y][x] = "#"

                            sidesteps_to_do -= 1
                            break

                    else:
                        if (
                            self.labyrinth.labyrinth_matrix[y + direction[0]][x + 1]
                            == "#"
                            and self.labyrinth.labyrinth_matrix[y + direction[0]][x - 1]
                            == "#"
                            and x > 0
                            and y + direction[0] >= 0
                        ):
                            self.labyrinth.labyrinth_matrix[y + direction[0]][
                                x + 1
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y + direction[0]][
                                x - 1
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y + direction[0]][x] = "."

                            self.labyrinth.broken_walls.append((y + direction[0], x))

                            self.labyrinth.labyrinth_matrix[y + (direction[0] // 2)][
                                x + 1
                            ] = "."
                            self.labyrinth.labyrinth_matrix[y + (direction[0] // 2)][
                                x - 1
                            ] = "."
                            self.labyrinth.broken_walls.append(
                                (y + (direction[0] // 2), x + 1)
                            )
                            self.labyrinth.broken_walls.append(
                                (y + (direction[0] // 2), x - 1)
                            )

                            self.labyrinth.labyrinth_matrix[y][x] = "#"

                            sidesteps_to_do -= 1
                            break
                except IndexError:
                    pass

        return self.labyrinth.labyrinth_matrix
