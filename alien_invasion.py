import sys

import pygame
from pygame.sprite import Group

from settings import Setting
from GameStats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf


def run_game():
	#Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Setting()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Create an instance to store game statistics.
	stats = GameStats(ai_settings)

	#Make a Ship, a grooop of bullets and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Set the Background Color.
	#bg_color = (230, 230, 230)
	#Make an alien
	#alien = Alien(ai_settings, screen)

	#Start the main loop for the game,
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		#redraw the screen during each pass through the loop
		# Not sure if this should be here: screen.fill(ai_settings.bg_color)
        # Not sure if this should be here: ship.blitme()

		#Watch for keyboard and mouse events.
		#for even in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()


		#Make the most reently drawn screen visible.
		#Not sure if this should be here: pygame.display.flip()
		#Irrelevant comment. Test.
run_game()