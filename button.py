import pygame.font  # .font allow pygame to render text on the screen


class Button:
    """ A Class to Create the Start Button
    """

    def __init__(self, ai_game, msg, center, color):
        """Initialize the button attributes"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.button_settings()

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = center # center button on the screen
        self.color = color  # button color

        # The button message need to be prepped only once
        self._prep_msg(msg)

    def button_settings(self):
        """Respond to the button settings"""
        # Set the dimenson and properties the of the button
        self.width, self.height = 200, 50 # width and height will be invert 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(
            'Times New Roman', bold=True, size=30, italic=True)

        self.hover_color = (100, 100, 255)

    def _hover_button_color(self):
        """Set the hover color"""
        self.button_color = self.hover_color

    def _prep_msg(self, msg,):
        """Trun msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.color, self.rect)  # draw the rectange
        # draw the text image
        self.screen.blit(self.msg_image, self.msg_image_rect)
