import pygame
from color import *

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

class Screen:
	class _Text:
		def __init__(self, key, text):
			if key == 'nan' or key == None:
				self.key = None
			else:
				self.key = eval('pygame.K_'+key)
			self.text = text

	def __init__(self, screen, *args, **kwargs):
		self.textlist = []
		for a in args:
			self.textlist.append(self._Text(None, a))
		self.screen = screen
		for k,v in kwargs.items():
			self.textlist.append(self._Text(k,v))

	def loop(self):
		self.screen.fill(black)
		for _t in self.textlist:
			_t.text.displaytext()
		pygame.display.update()

		while True:
			if xbutton():
				return pygame.K_q
			key = pygame.key.get_pressed()
			for _t in self.textlist:
				if _t.key == None:
					continue
				elif key[_t.key]:
					return _t.key