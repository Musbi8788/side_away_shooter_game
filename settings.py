class Settings:
    """A class to set the settings for the game
    """

    def __init__(self):
        """Initialize for the game
        """

        # Bullets Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3.5
        self.bullet_height = 15
        self.bullet_color = (75, 0, 130)

        # Ship Settings 
        self.ship_speed = 1.5

        # Screen Settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (47, 79, 79)
        self.game_title = "Ship Game"
