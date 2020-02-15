import pygame

class Ship:
	"""A class to manage the ship"""

	def __init__(self,ai_game):
		"""initialize the ship and set starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load(r'C:\Users\John Meister\Documents\Alien Invasion Python Game\images\ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		#Store a decimal value for the ships horizontal position.
		self.x = float(self.rect.x)

		#Movement Flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update the ship's position based on the movement flag"""
		#Update the ship's x value, not the rect.

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			self.rect.x += 1 
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			self.rect.x -= 1

		#Update rect object from self.x.
		self.rect.x = self.x	

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		


