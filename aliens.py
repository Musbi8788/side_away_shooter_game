import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    """

    def __init__(self, ss_game):
        """Initialize the alien and set it starting position.
        """
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the image and set it rect attributes
        self.image = pygame.image.load("images/alien.bmp")

        # Rotate the image to left
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()

        # Start each new alien near the topright of the screen
        self.rect.topright = (self.rect.width, self.rect.height)
        # self.rect.y = 900
        # self.rect.x = 0
        

        # Store the alien's exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen
        """
        # get the screen rect
        screen_rect = self.screen.get_rect()

        # checking the alien fleet position in the screen
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0: # determinding how to the alien should move on the screen
            return True

    def update(self):
        """Move the alien left or right
        """
        self.y -= (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y # update position of the alien rect
