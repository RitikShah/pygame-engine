import pygame
from color import *

class Text:
	def __init__(self, screen, text, color=white, size=20, xoffset=0, yoffset=0, xcenter=True, ycenter=True):
		windowsize = pygame.display.get_surface().get_size()
		self.text = str(text)
		self.font = pygame.font.Font('data/Courier New.ttf', size)
		self.screen = screen
		self.textsurf = self.font.render(self.text, True, color)
		self.textrect = self.textsurf.get_rect()
		self.textrect.center = (windowsize[0]/2)*xcenter + xoffset, (windowsize[1]/2)*ycenter + yoffset
	
	def displaytext(self):
		self.screen.blit(self.textsurf, self.textrect)