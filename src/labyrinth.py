import pygame

class Labyrinth:

    def __init__(self, width, height, steps_required) -> None:
        self.labyrinth = []
        self.width = width
        self.height = height
        self.steps_required = steps_required

        for i in range(0,2*height):
            self.labyrinth.append("#"*2*width)
    
    def set_labyrinth(self, labyrinth):
        self.labyrinth = labyrinth
        self.width = len(labyrinth[0])
        self.height = len(labyrinth)

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
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(sarake*cell_size, rivi*cell_size, cell_size + 1, cell_size))
        
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        
        pygame.quit()
