import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage a bullets fired from the ship

    Args:
        Sprite (model): pygame model
    """

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position

        Args:
            ai_game (model): alien invasion model
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet at (0, 0) and then set a correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        # Store the bullet position as a dicemal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen.
        """
        # Update the decimal position of the bullet
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
