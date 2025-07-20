import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """A class to manage the heart.
    """

    def __init__(self, ai_game):
        """Initialize the heart and set it starting position.

        Args:
            ai_game (_type_): _description_
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get it rect
        self.image = pygame.image.load('images/heart1.bmp')
        self.rect = self.image.get_rect()


        # Store a decimal value for the heart's vertical position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the heart at it current location.
        """
        self.screen.blit(self.image, self.rect)
