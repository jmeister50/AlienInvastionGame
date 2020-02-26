class Settings:
	"""A class to store all settings for alien invasion.""" 

	def __init__(self):
		"""Initialize the game's static settings."""
		#Settings screen
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#Bullet Settings
		self.bullet_speed = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Ship Settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		#Alien Settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#How quickly the game speeds up. 
		self.speeedup_scale = 1.1

		#How quickly the alien points value increases
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize the settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.alien_speed = 1.0

		#Fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase the speed settings and alien point values."""
		self.ship_speed *= self.speeedup_scale
		self.bullet_speed *= self.speeedup_scale
		self.alien_speed *=self.speeedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
		





