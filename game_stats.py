class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ss_game):
        """Initialize the game statistics"""
        self.settings = ss_game.settings
        self.rest_stats()

        # Start an Alien Invasion in an active state
        self.game_active = True

    def rest_stats(self,):
        """Initialize statistics that can change during the game."""
        
        self.ships_left -= self.settings.ship_limit