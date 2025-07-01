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
        self.screen_width = 850
        self.screen_height = 650
        self.bg_color = (130, 200, 229)
        self.game_title = "Ship Game"
