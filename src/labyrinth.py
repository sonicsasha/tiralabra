import pygame
import random

class UserInputError(Exception):
    pass

class Labyrinth:

    def __init__(self, width : int, height : int, steps_required : int) -> None:
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
            UserInputError: The user tries to complete a labyrinth in an amount of steps that doesn't satisfy the condition of required steps.
        """
        min_step_count = width + height - 2
        if (width==1 and height==1):
            raise UserInputError ("Ei voida luoda 1x1 labyrinttiä")
        
        elif (width % 2 == 0 or height % 2 == 0):
            raise UserInputError ("Labyrintin leveyden ja korkeuden täytyy olla parittomia lukuja.")
        
        elif (min_step_count > steps_required):
            raise UserInputError (f"""Annetun kokoista labyrinttiä ei pysty ratkaisemaan annetussa määrässä askelia.
                                    Ole hyvä ja anna joko pienempi labyrintin koko tai suurempi määrä askelia.
                                    Pienin määrä askelia annetuulla koolla on {min_step_count}""")
    

        elif (steps_required - min_step_count)%4 != 0:
            raise UserInputError(f"""Annetun kokoista labyrinttiä ei pysty ratkaisemaan annetussa määrässä askelia.
                                    Ole hyvä, ja anna joko eri labyrintin koko tai eri määrä askelia.
                                    Lähimmät mahdolliset askeleet ovat {((steps_required)//4)*4} ja {((steps_required)//4)*4 + 4}""")

        self.labyrinth_matrix = []
        self.width = width
        self.height = height
        self.steps_required = steps_required

        # If conditions are met and everything is alright, generate an "empty" maze filled with "#"

        for i in range(0,height):
            self.labyrinth_matrix.append(["#"]*width)
    
    # def set_labyrinth(self, labyrinth : list):
    #     """Manually sets a labyrinth. Mostly used for testing.

    #     Args:
    #         labyrinth (list): A matrix of a labyrinth, where "." represents a path and "#" represents a wall.
    #     """        
    #     self.labyrinth_matrix = labyrinth
    #     self.width = len(labyrinth[0])
    #     self.height = len(labyrinth)
    
    def generate_path_start_to_finish(self):
        """Creates a random path from the lower left corner of the labyrinth to the upper right corner.

        Raises:
            UserInputError: If a path cannot be generated, then that probably means that the steps required is too high
        """        
        self.path_found = False
        shortest_taxi_distance = self.width + self.height - 2

        sidesteps_left = self.steps_required-shortest_taxi_distance

        self.generate_path_recursion(self.height-1, 0, self.steps_required, sidesteps_left)

        if not self.path_found:
            raise UserInputError("Labyrintin generointi ei onnistunut. Ongelma johtuu todennäköisesti siitä, että askelten määrä on liian iso.")
    
    def generate_path_recursion(self, y:int, x:int, steps_left:int, sidesteps_left:int):
        """FUNCTION WILL BE DEPRECATED SOON

        Args:
            y (int): _description_
            x (int): _description_
            steps_left (int): _description_
            sidesteps_left (int): _description_

        Raises:
            IndexError: _description_
            IndexError: _description_
            IndexError: _description_
        """        
        self.labyrinth_matrix[y][x] = "."

        if (y,x) == (0,self.width-1) and steps_left==0:
            self.path_found = True
            return
        
        #The below line is excluded from coverage reporting, since there is only a small chance that the below piece of code is executed.
        elif steps_left==0 or sidesteps_left<0: #pragma: no cover
            return



        p = (sidesteps_left/2) / (steps_left-(sidesteps_left/2))

        if random.random()<p:
            sidestep = True
        else:
            sidestep = False
        
        if sidestep:
            directions = ([(0,-2), (2,0)])
            random.shuffle(directions)
            directions += [(-2,0),(0,2)]
        else:
            directions = [(-2,0),(0,2)]
            random.shuffle(directions)
            directions += [(0,-2), (2,0)]
        
        for direction in directions:
            try:
                if y + direction[0] < 0 or x + direction[1] < 0:
                    raise IndexError
                
                if (x == 0 or x==self.width-1) and direction == (2,0):
                    raise IndexError
                
                if (y == 0 or y==self.height - 1) and direction == (0,-2):
                    raise IndexError

                
                if self.labyrinth_matrix[y + direction[0]][x + direction[1]] == "#":
                    self.labyrinth_matrix[y + direction[0]//2][x + direction[1]//2] = "."

                    is_sidestepping = (direction == (0,-2) or direction == (2,0))
                    self.generate_path_recursion(y + direction[0], x + direction[1], steps_left - 2, sidesteps_left - int(is_sidestepping) * 4)
                    if self.path_found:
                        break
                    self.labyrinth_matrix[y + direction[0]//2][x + direction[1]//2] = "#"
                    self.labyrinth_matrix[y + direction[0]][x + direction[1]] = "#"
            except IndexError:
                pass

    def generate_maze_around_path(self):
        """Given that a random path from start to finish has been generated, generate a maze around that path

        Returns:
            list: A matrix representing the labyrinth.
        """

        #Check the path which has been generated. This will allow the program to randomly choose a cell from which to start generating the maze.
        path_cells = []

        for i in range(len(self.labyrinth_matrix)):
            for j in range(len(self.labyrinth_matrix[i])):
                if self.labyrinth_matrix[i][j]=="." and i%2 == 0 and j%2 == 0 and not (i==0 and j==self.width-1):
                    path_cells.append((i,j))
        
        #Go through every cell in the path so that there is a path in every area of the maze.

        random.shuffle(path_cells)

        directions = [(-2,0), (2,0), (0,2), (0,-2)]

        for cell in path_cells:
            random.shuffle(directions)

            #Try to start a depth search in every direction until it can be started.
            for direction in directions:
                try:
                    if cell[0] + direction[0] < 0 or cell[1] + direction[1] < 0:
                        continue

                    if self.labyrinth_matrix[cell[0] + direction[0]][cell[1] + direction[1]] == "#":
                        self.labyrinth_matrix[cell[0] + direction[0]//2][cell[1] + direction[1]//2] = "."
                        self.generate_random_path(cell[0] + direction[0], cell[1] + direction[1])
                except IndexError:
                    pass
        
        return self.labyrinth_matrix

    def generate_random_path(self, y : int, x : int):
        """Given a cell, start a randomized depth search from said cell and generate a maze from said cell

        Args:
            y (int): The y coordinate of the cell from which the depth search will start.
            x (int): The x coordinate of the cell from which the depth search will start.
        """        
        stack = []
        #Whenever we move in a certain direction in a maze, we have to move two steps. That's why we add a tuple consisting of two tuples to the stack.
        stack.append(((y,x),(y,x)))
        directions = [(-2,0), (2,0), (0,2), (0,-2)]
        while len(stack)!=0:
            current = stack.pop()
            wall_break = current[0]
            new_cell = current[1]
            if self.labyrinth_matrix[new_cell[0]][new_cell[1]] == "#" and self.labyrinth_matrix[wall_break[0]][wall_break[1]] == "#":
                #Clear the currently selected cells.
                self.labyrinth_matrix[new_cell[0]][new_cell[1]] = "."
                self.labyrinth_matrix[wall_break[0]][wall_break[1]] = "."
                random.shuffle(directions)
                #Add all the directions we can move in to the stack.
                for direction in directions:
                    try:
                        if new_cell[0] + direction[0] < 0 or new_cell[1] + direction[1] < 0:
                            continue

                        if self.labyrinth_matrix[new_cell[0] + direction[0]][new_cell[1] + direction[1]] == "#":
                            stack.append(((new_cell[0]+direction[0]//2,new_cell[1] + direction[1]//2),(new_cell[0] + direction[0], new_cell[1] + direction[1])))
                    
                    except IndexError:
                        pass





