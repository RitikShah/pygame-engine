import pygame
class World:
	def __init__(self, width, height):
		self.window = (width, height)
		self.tick 	= 0

		# Contains all sprites
		self.all_sprites = pygame.sprite.Group()

	def update(self):
		tick += 1