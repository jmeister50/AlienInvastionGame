class GameStats:
	"""Tracks stats for Alien Invasion"""
	def __init__(self, ai_game):
		"""Initialize stats."""
		#High score should never be reset.
		self.high_score = 0
		self.settings = ai_game.settings
		self.reset_stats()
		#Start Alien Invasion in an inactive state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize stats that can change during game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		


		