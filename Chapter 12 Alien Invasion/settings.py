class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings (appearance and ship speed)."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)     # tuple due to ()
        self.bg_color = (135, 206, 235)     # 12-1 blue sky color

        # Ship settings
        self.ship_speed = 1.2   # sets the pixels to 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
