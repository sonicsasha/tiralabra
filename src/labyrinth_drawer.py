import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "true"
import pygame


class Button:
    """This is a class used for creating buttons in the pygame view."""

    def __init__(self, pos, size, button_text, labyrinth_to_draw):
        x = pos[0]
        y = pos[1]
        width = size[0]
        height = size[1]
        self.labyrinth_to_draw = labyrinth_to_draw

        font = pygame.font.SysFont("Arial", 20)

        self.fill_colors = {
            "normal": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
        }

        self.button_surface = pygame.Surface((width, height))
        self.button_rect = pygame.Rect(x, y, width, height)

        self.button_text = font.render(button_text, True, (20, 20, 20))

    def check_click(self):
        """Checks if the user is clicking the button

        Returns:
            Labyrinth: Returns the labyrinth assigned to the button if the user clicks the button.
        """
        mouse_pos = pygame.mouse.get_pos()
        self.button_surface.fill(self.fill_colors["normal"])
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors["hover"])
            if pygame.mouse.get_pressed()[0]:
                self.button_surface.fill(self.fill_colors["pressed"])
                return self.labyrinth_to_draw

        return None

    def draw_text_on_button(self):
        """Draws the text on top of the button."""
        self.button_surface.blit(
            self.button_text,
            [
                self.button_rect.width / 2 - self.button_text.get_rect().width / 2,
                self.button_rect.height / 2 - self.button_text.get_rect().height / 2,
            ],
        )


class LabyrinthDrawer:
    """Class used to draw a list of labyrinths with the ability to choose
    which labyrinth to draw."""

    def __init__(self, labyrinths: list):
        """Draws the labyrinth

        Args:
            labyrinths (list):  List of tuples, where the first elements is of a Labyrinth class
                                and the second element is the text shown on the button.
        """
        pygame.init()
        self.buttons = []

        # How much space should be left in the top bar.
        self.overhead = 50

        button_x = 5
        button_y = 10
        button_height = 30
        button_width = 240
        # Labyrinths are stored in a list of tuples,
        # where the first element of the tuple is the labyrinth
        # and the second element is the name shown on the button
        for labyrinth in labyrinths:
            button_text = labyrinth[1]
            labyrinth_to_show_on_click = labyrinth[0]
            self.buttons.append(
                Button(
                    (button_x, button_y),
                    (button_width, button_height),
                    button_text,
                    labyrinth_to_show_on_click
                )
            )
            button_x += button_width + 10

        self.labyrinth_to_draw = labyrinths[-1][0]

        self.screen_width = 1000
        self.cell_size = self.screen_width / self.labyrinth_to_draw.width
        screen_height = self.cell_size * self.labyrinth_to_draw.height + self.overhead
        self.screen = pygame.display.set_mode([self.screen_width, screen_height])
        pygame.display.set_caption("MazeGen")

        self.draw_loop()

    def draw_loop(self):
        """The main loop of the pygame instance. Draws the screen and checks the button clicks."""
        self.draw_labyrinth()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for button in self.buttons:
                new_labyrinth = button.check_click()
                if new_labyrinth is not None:
                    self.labyrinth_to_draw = new_labyrinth
                    self.draw_labyrinth()
                button.draw_text_on_button()
                self.screen.blit(button.button_surface, button.button_rect)

            pygame.display.flip()

        pygame.quit()

    def draw_labyrinth(self):
        """Draws the labyrinth in the bottom part of the screen
        where every wall is black and every empty cell is white.
        """
        self.screen.fill((255, 255, 255))

        pygame.draw.rect(
            self.screen,
            (128, 128, 128),
            pygame.Rect(0, 0, self.screen_width, self.overhead),
        )

        for row_number, row in enumerate(self.labyrinth_to_draw.labyrinth_matrix):
            for column in enumerate(row):
                column_number = column[0]
                if (
                    self.labyrinth_to_draw.labyrinth_matrix[row_number][column_number]
                    == "#"
                ):
                    pygame.draw.rect(
                        self.screen,
                        (0, 0, 0),
                        pygame.Rect(
                            column_number * self.cell_size,
                            row_number * self.cell_size + self.overhead,
                            self.cell_size + 1,
                            self.cell_size + 1,
                        ),
                    )
