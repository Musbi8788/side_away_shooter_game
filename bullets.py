import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """A class to manage the bullet game

    Args:
        Sprite (_type_): _description_
    """

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet at (0 ,0) and then set it correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        
        # Store the bullet position as a decimal value
        self.x = float(self.rect.x)

    def updata(self):
        """Moving the bullet right side of the screen
        """
        self.x += self.settings.bullet_speed
        # Update the rect object
        self.rect.x = self.x

    def draw_bullets(self):
        """Draw the game bullets
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
    