import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 13 - Aliens/images/water.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact veritcal position.
        self.y = float(self.rect.y)

    def check_rain_edges(self):
        """Return True if raindrops are at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom <= screen_rect.bottom:
            return True

    def update(self):
        """Move the rain to the bottom."""
        self.y += (self.settings.raindrop_speed)
        self.rect.x = self.x