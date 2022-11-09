import pygame
from labyrinth import Labyrinth

def draw_labyrinth(labyrinth : Labyrinth):
    """Draws the labyrinth of the class using pygame. WILL BE DEPRECATED.
    """        
    screen_width = 1000
    cell_size = screen_width / labyrinth.width
    screen_height = cell_size * labyrinth.height

    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])

    screen.fill((255, 255, 255))

    for row in range(0,len(labyrinth.labyrinth_matrix)):
        for column in range(0,len(labyrinth.labyrinth_matrix[0])):
            if labyrinth.labyrinth_matrix[row][column] == "#":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(column*cell_size, row*cell_size, cell_size + 1, cell_size + 1))
    
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
    pygame.quit()