class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings (appearance and ship speed)."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     # tuple due to ()
        # self.bg_color = (135, 206, 235)     # 12-1 blue sky color

        # Ship settings
        self.ship_speed = 1.0   # sets the pixels to 1.5
        
        # Bullet settings
        self.bullet_speed = 1.4
        self.bullet_width = 500
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 = moves right; -1 moves left.
        self.fleet_direction = 1

        # Raindrop settings
        self.raindrop_speed = 1.0
        self.raindrop_drop_speed = 10     