import pygame
import random

class UserInputError(Exception):
    pass

class Labyrinth:

    def __init__(self, width, height, steps_required) -> None:

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

        self.labyrinth = []
        self.width = width
        self.height = height
        self.steps_required = steps_required

        for i in range(0,height):
            self.labyrinth.append(["#"]*width)
    
    def set_labyrinth(self, labyrinth):
        self.labyrinth = labyrinth
        self.width = len(labyrinth[0])
        self.height = len(labyrinth)
    
    def generate_path_start_to_finish(self):
        self.path_found = False
        shortest_taxi_distance = self.width + self.height - 2

        sidesteps_left = self.steps_required-shortest_taxi_distance

        self.generate_path_recursion(self.height-1, 0, self.steps_required, sidesteps_left)

        if not self.path_found:
            raise UserInputError("Labyrintin generointi ei onnistunut. Ongelma johtuu todennäköisesti siitä, että askelten määrä on liian iso.")
    
    def generate_path_recursion(self, y:int, x:int, steps_left:int, sidesteps_left:int):
        self.labyrinth[y][x] = "."

        if (y,x) == (0,self.width-1) and steps_left==0:
            self.path_found = True
            return
        
        elif steps_left==0 or sidesteps_left<0:
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

                
                if self.labyrinth[y + direction[0]][x + direction[1]] == "#":
                    self.labyrinth[y + direction[0]//2][x + direction[1]//2] = "."

                    is_sidestepping = (direction == (0,-2) or direction == (2,0))
                    self.generate_path_recursion(y + direction[0], x + direction[1], steps_left - 2, sidesteps_left - int(is_sidestepping) * 4)
                    if self.path_found:
                        break
                    self.labyrinth[y + direction[0]//2][x + direction[1]//2] = "#"
                    self.labyrinth[y + direction[0]][x + direction[1]] = "#"
            except IndexError:
                pass

    def generate_maze_around_path(self):
        path_cells = []

        for i in range(len(self.labyrinth)):
            for j in range(len(self.labyrinth[i])):
                if self.labyrinth[i][j]=="." and i%2 == 0 and j%2 == 0:
                    path_cells.append((i,j))
        
        random.shuffle(path_cells)

        directions = [(-2,0), (2,0), (0,2), (0,-2)]

        for cell in path_cells:
            random.shuffle(directions)

            for direction in directions:
                try:
                    if cell[0] + direction[0] < 0 or cell[1] + direction[1] < 0:
                        continue

                    if self.labyrinth[cell[0] + direction[0]][cell[1] + direction[1]] == "#":
                        self.labyrinth[cell[0] + direction[0]//2][cell[1] + direction[1]//2] = "."
                        self.generate_random_path(cell[0] + direction[0], cell[1] + direction[1])
                except IndexError:
                    pass

    def generate_random_path(self, y, x):
        stack = []
        stack.append(((y,x),(y,x)))
        directions = [(-2,0), (2,0), (0,2), (0,-2)]
        while len(stack)!=0:
            current = stack.pop()
            wall_break = current[0]
            new_cell = current[1]
            if self.labyrinth[new_cell[0]][new_cell[1]] == "#" and self.labyrinth[wall_break[0]][wall_break[1]] == "#":
                self.labyrinth[new_cell[0]][new_cell[1]] = "."
                self.labyrinth[wall_break[0]][wall_break[1]] = "."
                random.shuffle(directions)
                for direction in directions:
                    try:
                        if new_cell[0] + direction[0] < 0 or new_cell[1] + direction[1] < 0:
                            continue

                        if self.labyrinth[new_cell[0] + direction[0]][new_cell[1] + direction[1]] == "#":
                            stack.append(((new_cell[0]+direction[0]//2,new_cell[1] + direction[1]//2),(new_cell[0] + direction[0], new_cell[1] + direction[1])))
                    
                    except IndexError:
                        pass




    def draw_labyrinth(self):
        screen_width = 1000
        cell_size = screen_width / self.width
        screen_height = cell_size * self.height

        pygame.init()
        screen = pygame.display.set_mode([screen_width, screen_height])

        screen.fill((255, 255, 255))

        for rivi in range(0,len(self.labyrinth)):
            for sarake in range(0,len(self.labyrinth[0])):
                if self.labyrinth[rivi][sarake] == "#":
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(sarake*cell_size, rivi*cell_size, cell_size + 1, cell_size + 1))
        
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        
        pygame.quit()
