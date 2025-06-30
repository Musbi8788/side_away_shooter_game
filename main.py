import pygame

class SideWayShip():
    """A class manage the side away ship game
    """

    def __init__(self, ):
        """Initialize the game's resources
        """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("side away shooting")

        