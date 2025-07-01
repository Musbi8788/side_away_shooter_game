import sys
import pygame
from settings import Settings
from ship import Ship

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

        self.ship = Ship(self)


    def run_game(self):
        """manage the game running
        """
        game_is_running = True
        while game_is_running:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypress
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress
        """
        # move the ship up
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to key release

        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False



    def _update_screen(self):
        """Update the screen background and show the image 
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    rg = SideWayShip()
    rg.run_game()
