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
