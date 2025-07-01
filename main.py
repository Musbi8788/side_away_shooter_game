import sys
import pygame
from settings import Settings

class SideWayShip():
    """A class manage the side away ship game
    """

    def __init__(self, ):
        """Initialize the game's resources
        """
        pygame.init()
        self.settings = Settings()

        # using the screen setttings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        # load the game image 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, -90)


        # set the position of the image in the screen
        self.screen_rect = self.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft
    def run_game(self):
        """manage the game running
        """
        game_is_running = True
        while game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()


    def _update_screen(self):
        """Update the screen background and show the image 
        """
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()


if __name__ == "__main__":
    rg = SideWayShip()
    rg.run_game()
