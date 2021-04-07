import sys
sys.path.append('/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 13 - Aliens')  
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:
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
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()
        self._create_stars()
        # Set the background color (RGB)
        # self.bg_color = (230, 230, 230)

    # Game is controlled by run_game()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()    # detects relevant key/mouse events
            self.ship.update()      # updates the ship's location
            self._update_bullets()   # updates all bullets position
            self._update_aliens()   # updates alien positions
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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))        # prints # of bullets on screen for debugging

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)   # Pygame draws each element at the pos defined by its rect attribute.
        self.stars.draw(self.screen)   # Pygame draws each element at the pos defined by its rect attribute.
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)  # 2 b/c alien + alien space
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):    
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

# Below is the fleet of Stars from Exercise 13-1 and 13-2.
    def _create_stars(self):
        """Create the fleet of stars."""
        # Make an star.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)  # 2 b/c star + star space
        number_stars_x = available_space_x // (2 * star_width)
        
        # Determine the number of rows of stars that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * star_height) - ship_height)
        number_rows = available_space_y // (2 * star_height)
        
        # Create the full fleet of stars.
        for row_number in range(number_rows):    
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        # Create an star and place it in the row.
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x + randint(-30, 30)
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number + randint(-30, 30)
        self.stars.add(star)

    def _update_aliens(self):
        """Check if the fleet is at an edge, 
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()