import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # surface in Pygame where a game element can be displayed
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
        self.settings.screen_height))  # width x height from Settings
        pygame.display.set_caption("Alien Invasion")

        # Set the background color (RGB)
        # self.bg_color = (230, 230, 230)

    # Game is controlled by run_game()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse "events"
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.Settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()