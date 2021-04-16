# %%
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class SidewayShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # surface in Pygame where a game element can be displayed
        # Windowed Mode Below 
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # width x height from Settings
        
        # Full Screen Mode Below 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color (RGB)
        # self.bg_color = (230, 230, 230)

    # Game is controlled by run_game()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()    # detects relevant key/mouse events
            self.ship.update()      # updates the ship's location
            self._update_bullets()   # updates all bullets position
            self._update_screen()   # redraws the screen on each pass of main loop

    def _check_events(self):
        # Watch for keyboard and mouse "events"
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right by flagging ship.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left by flagging ship.
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            # Move the ship to the right by flagging ship.
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship to the left by flagging ship.
            self.ship.moving_down = True
        elif event.key == pygame.K_q:  # Exits alien_invasion.py if Q is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """Responds to key releases."""
        # if keys let go/up, then disable flagging ship        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and ADDS it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        
        # Get rid of bullets that have dissapeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
        # print(len(self.bullets))        # prints # of bullets on screen for debugging

    def _create_fleet(self):
        """Create the fleet of alien ships."""

        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)
        
# available_space_x = settings.screen_width - (2 * alien_width)
# number_aliens_x = available_space_x // (2 * alien_width)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewayShooter()
    ss.run_game()
# %%
