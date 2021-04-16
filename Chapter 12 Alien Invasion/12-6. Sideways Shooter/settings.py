class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings (appearance and ship speed)."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (64, 64, 64)     # tuple due to () grey sky color
        # self.bg_color = (135, 206, 235)     # 12-1 blue sky color

        # Ship settings
        self.ship_speed = .5   # sets the pixels to 1.5
        

        # Bullet settings
        # self.image = pygame.image.load('/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 12 Alien Invasion/12-6. Sideways Shooter/images/shot1_1.png')
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (50, 250, 50)
        self.bullets_allowed = 5

        # Aliens settings
        self.alien_speed = 1.0
        self.fleet_direction = 1.0