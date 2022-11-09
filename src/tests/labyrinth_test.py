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
        maze = Labyrinth(3,3,124)
        self.assertRaises(UserInputError, maze.generate_path_start_to_finish)
    
    def test_can_create_maze_with_valid_inputs(self):
        maze = Labyrinth(5,5,12)
        self.assertNotEqual(maze.labyrinth_matrix, None)
    
    def test_set_labyrinth(self):
        maze = Labyrinth()

class TestLabyrinthFeatures(unittest.TestCase):
    def setup_class(self):
        self.maze = Labyrinth(11,11,36)
        self.maze.generate_path_start_to_finish()
        self.maze.generate_maze_around_path()

    def test_can_reach_every_cell_from_start(self):
        dfs_matrix = []

        for i in range(self.maze.height):
            dfs_matrix.append(["#"]*self.maze.width)
        
        stack = []
        stack.append((self.maze.height-1,0))

        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        while len(stack)>0:
            current_cell = stack.pop()
            y = current_cell[0]
            x = current_cell[1]

            if y<0 or x<0:
                continue
            
            
            if self.maze.labyrinth_matrix[y][x]=="." and dfs_matrix[y][x]=="#":
                dfs_matrix[y][x]="."
                for direction in directions:
                    try:
                        if self.maze.labyrinth_matrix[y + direction[0]][x + direction[1]] == ".":
                            stack.append((y + direction[0], x + direction[1]))
                    except IndexError:
                        pass
        
        self.assertEqual(self.maze.labyrinth_matrix, dfs_matrix)
    
    def test_goal_is_reached_in_required_amount_of_steps(self):
        bfs_matrix = []

        for i in range(self.maze.height):
            bfs_matrix.append([float("inf")]*self.maze.width)
        
        stack = []
        stack.append(((self.maze.height-1, 0), 0))

        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        while len(stack)>0:
            current_cell = stack.pop()
            y=current_cell[0][0]
            x=current_cell[0][1]
            distance = current_cell[1]

            if not distance<bfs_matrix[y][x]:
                continue
        
            if x<0 or y<0:
                continue
            
            bfs_matrix[y][x]=distance

            for direction in directions:
                try:
                    if self.maze.labyrinth_matrix[y + direction[0]][x + direction[1]]=="." and bfs_matrix[y + direction[0]][x + direction[1]] == float("inf"):
                        stack.append(((y + direction[0], x + direction[1]), distance + 1))
                except IndexError:
                    pass
        
        self.assertEqual(bfs_matrix[0][self.maze.width-1], self.maze.steps_required)

