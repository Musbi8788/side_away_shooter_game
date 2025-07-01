import pygame

class Ship:
    """A class to manage the ship
    """

    def __init__(self, ai_game):
        """Initialize the ship and set it starting position

        Args:
            ai_game (_type_): settings model
        """

        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the game image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Rotate the image to left
        self.image = pygame.transform.rotate(self.image, -90)

        # set the position of the image in the screen
        self.screen_rect = self.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Store the decimal value for the ship's vertical position
        self.y = float(self.rect.y)

        # Movement Flag
        self.moving_top = False
        self.moving_down = False

    def update(self):
        """update the ship current position base on the moving flag
        """
        # update the ship's x value not the self.rect
        # move the ship top
        if self.moving_top and self.rect.top < self.screen_rect.top:
            self.y += self.settings.ship_speed

        # move the ship down
        if self.moving_down and self.rect.bottom > self.screen_rect.bottom:
            self.y -= self.settings.ship_speed

        # Update the rect object from self.y
        self.rect.y = int(self.y)

    def blitme(self):
        """Draw the ship at it current position
        """
        self.screen.blit(self.image, self.rect)
        






