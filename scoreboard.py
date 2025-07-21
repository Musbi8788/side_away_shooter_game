import pygame.font
from pygame.sprite import Group  # We are importing a group of life

from life import Life


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize the scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.level_color = (78, 181, 135)
        self.score_color = self.settings.secondary_color
        self.high_score_color = (0, 100, 0)
        # set the font size and use defualt font style.
        self.font = pygame.font.SysFont(
            'Arial', bold=True, size=30, italic=True)

        self.prep_images()

    def prep_images(self,):
        """Prepare the initail images"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lifes()

    def prep_lifes(self):
        """Show how many lifes left."""
        self.lifes = Group()  # set the lifes group
        for life_number in range(self.stats.ships_left):  # display the ships left
            life = Life(self.ai_game)  # create an instance of life
            # Position the lifes left to the right top of the screen

            life.rect.y = 10 + life_number * life.rect.height
            life.rect.x = 1300

            self.lifes.add(life)  # add the lifes
            """this make the ship appear next to each other (-_-)  (-_-)  (-_-) """
            

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "  Level: " + str(self.stats.level)
        self.level_image = self.font.render(
            # generate the level text image
            level_str, True, self.level_color)
        
        # Rotate game level text
        self.level_image = pygame.transform.rotate(self.level_image, -90)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right

        self.level_rect.right = self.score_rect.left + \
            -25  # position the level under the life

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -
                            1)  # round the number eg 100000 to 10,000
        # add comma to the score
        score_str = "Score: " + "{:,}".format(rounded_score)

        self.score_image = self.font.render(
            score_str, True, self.score_color)

        # Rotate the score to left
        self.score_image = pygame.transform.rotate(
            self.score_image, -90)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 560

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, - 1)
        self.high_score_str = "High Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            self.high_score_str, True, self.high_score_color)
        
        # Rotate the high score to left
        self.high_score_image = pygame.transform.rotate(
            self.high_score_image, -90)

        self.center_high_score()

    def center_high_score(self):
        """Center the game high score."""
        # Center the high score at the top of the screen.
        # get the rect position of the high score
        self.high_score_rect = self.high_score_image.get_rect()
        # set the high score at the center
        self.high_score_rect.centery = self.screen_rect.centery  

        # position the high score at the top
        self.high_score_rect.right = self.score_rect.right  


    def check_high_score(self):
            """Check to see if there's a new high score."""
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score  # Update the high score
                self.prep_high_score()  # Update high score image

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lifes.draw(self.screen)  # Draw the lifes
