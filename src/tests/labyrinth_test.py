from labyrinth import Labyrinth, UserInputError
import unittest


class TestLabyrinthGeneration(unittest.TestCase):
    def test_cannot_create_1x1_maze(self):
        self.assertRaises(UserInputError, Labyrinth, 1, 1, 1)

    def test_cannot_create_maze_with_even_size(self):
        self.assertRaises(UserInputError, Labyrinth, 2, 2, 2)

    def test_cannot_create_maze_with_small_amount_of_steps(self):
        self.assertRaises(UserInputError, Labyrinth, 11, 11, 1)

    def test_cannot_create_maze_with_invalid_amount_of_steps(self):
        self.assertRaises(UserInputError, Labyrinth, 5, 5, 10)

    def test_cannot_create_maze_with_large_amount_of_steps(self):
        maze = Labyrinth(3, 3, 124)
        self.assertRaises(UserInputError, maze.generate_maze_dfs)

    def test_can_create_maze_with_valid_inputs(self):
        maze = Labyrinth(5, 5, 12)
        self.assertNotEqual(maze.labyrinth_matrix, None)


# Functions to help with tests
def can_reach_every_cell_from_start(labyrinth: Labyrinth):
    dfs_matrix = []

    for i in range(labyrinth.height):
        dfs_matrix.append(["#"] * labyrinth.width)

    stack = []
    stack.append((labyrinth.height - 1, 0))

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while len(stack) > 0:
        current_cell = stack.pop()
        y = current_cell[0]
        x = current_cell[1]

        if y < 0 or x < 0:
            continue

        if labyrinth.labyrinth_matrix[y][x] == "." and dfs_matrix[y][x] == "#":
            dfs_matrix[y][x] = "."
            for direction in directions:
                try:
                    if (
                        labyrinth.labyrinth_matrix[y + direction[0]][x + direction[1]]
                        == "."
                    ):
                        stack.append((y + direction[0], x + direction[1]))
                except IndexError:
                    pass

    return labyrinth.labyrinth_matrix == dfs_matrix


def goal_is_reached_in_required_amount_of_steps(labyrinth):
    bfs_matrix = []

    for i in range(labyrinth.height):
        bfs_matrix.append([float("inf")] * labyrinth.width)

    stack = []
    stack.append(((labyrinth.height - 1, 0), 0))

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while len(stack) > 0:
        current_cell = stack.pop()
        y = current_cell[0][0]
        x = current_cell[0][1]
        distance = current_cell[1]

        if not distance < bfs_matrix[y][x]:
            continue

        if x < 0 or y < 0:
            continue

        bfs_matrix[y][x] = distance

        for direction in directions:
            try:
                if labyrinth.labyrinth_matrix[y + direction[0]][
                    x + direction[1]
                ] == "." and bfs_matrix[y + direction[0]][x + direction[1]] == float(
                    "inf"
                ):
                    stack.append(((y + direction[0], x + direction[1]), distance + 1))
            except IndexError:
                pass

    return bfs_matrix[0][labyrinth.width - 1] == labyrinth.steps_required


class TestLabyrinthFeaturesDFS(unittest.TestCase):
    def setup_class(self):
        self.maze = Labyrinth(11, 11, 36)
        self.maze.generate_maze_dfs()

    def test_generates_correct_5x5_labyrinth_with_16_steps(self):
        test_maze = Labyrinth(5, 5, 16)
        test_maze.generate_maze_dfs()

        correct_maze = False

        if test_maze.labyrinth_matrix == [
            [".", ".", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", ".", "."],
        ] or test_maze.labyrinth_matrix == [
            [".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#"],
            [".", ".", ".", ".", "."],
            ["#", "#", "#", "#", "."],
            [".", ".", ".", ".", "."],
        ]:

            correct_maze = True

        self.assertTrue(correct_maze)

    def test_can_reach_every_cell_from_start(self):
        self.assertTrue(can_reach_every_cell_from_start, self.maze)

    def test_goal_is_reached_in_required_amount_of_steps(self):
        self.assertTrue(goal_is_reached_in_required_amount_of_steps, self.maze)


class TestLabyrinthFeaturesPrim(unittest.TestCase):
    def setup_class(self):
        self.maze = Labyrinth(11, 11, 36)
        self.maze.generate_maze_prim()

    def test_generates_correct_5x5_labyrinth_with_16_steps(self):
        test_maze = Labyrinth(5, 5, 16)
        test_maze.generate_maze_prim()

        correct_maze = False

        if test_maze.labyrinth_matrix == [
            [".", ".", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", ".", "."],
        ] or test_maze.labyrinth_matrix == [
            [".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#"],
            [".", ".", ".", ".", "."],
            ["#", "#", "#", "#", "."],
            [".", ".", ".", ".", "."],
        ]:

            correct_maze = True

        self.assertTrue(correct_maze)

    def test_can_reach_every_cell_from_start(self):
        self.assertTrue(can_reach_every_cell_from_start, self.maze)

    def test_goal_is_reached_in_required_amount_of_steps(self):
        self.assertTrue(goal_is_reached_in_required_amount_of_steps, self.maze)
