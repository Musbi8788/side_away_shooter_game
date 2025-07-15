import sys
import pygame

from ship import Ship
from bullets import Bullet
from settings import Settings
from aliens import Alien

class SideWayShip():
    """A class manage the side away ship game
    """

    def __init__(self, ):
        """Initialize the game's resources
        """
        pygame.init()
        self.settings = Settings()

        # Using the screen setttings

        # Defualt screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # # FullScreen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.screen_width = self.screen.get_rect().width
        # self.screen_height = self.screen.get_rect().height


        pygame.display.set_caption(self.settings.game_title)

        self.ship = Ship(self)
        # Make the bullets and aliens in a pygame group form
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # create fleet mean group of aliens
        self._create_fleet()

    def run_game(self):
        """manage the game running
        """
        game_is_running = True
        while game_is_running:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
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


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group
        """
        # Limit the bullets showing in the game screen
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

        self._check_bullets_aliens_collisions()

    def _check_bullets_aliens_collisions(self):
        """Respond to bullets-aliens collisions
        """
        # Remove any bullets and aliens that have collided

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, True)  # change False to True after

        # if aliens don't exist create a new fleet of aliens
        if not self.aliens:
            # Destory existing bullets and create new fleet
            self.aliens.empty()  # destory the aliens
            self._create_fleet()  # create new fleet of aliens

    def _create_fleet(self):
        """Create the fleet of alien
        """
        # Create an alien and find the number of an aliens in a column
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)  # alien use for calculation and spacing
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        # Determine the number of aliens that fit on the screen
        ship_width = self.ship.rect.width
        available_space_y = (self.settings.screen_width -
                             (2 * alien_width) - ship_width)
        
        number_columns = available_space_y // (2 * alien_width)  # defualt is 2

        # Create the full fleet of aliens
        for column_number in range(number_columns):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, column_number)

    def _create_alien(self, alien_number, column_number):
        """Create an alien
        """
        # Create an alien and place it in the column
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y

        alien.rect.right = self.settings.screen_width - 2 * alien_width * column_number
        
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if an alien is at edge, 
            then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges(
            # checking the position of the alien and determinding an action to do with each fleet.
        )
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():  # call check edges funtion in alien.py
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """Update position of bullet and get rid of the old bullet
        """
        # Get rid of bullets that has disappeared
        for bullet in self.bullets.copy():
            # place i get stuck with 
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)


    def _update_screen(self):
        """Update the screen background and show the image 
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    rg = SideWayShip()
    rg.run_game()
