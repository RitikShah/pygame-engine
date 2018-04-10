import pygame
from color import *

class Text:
	def __init__(self, screen, text, color=white, size=20, xoffset=0, yoffset=0, xcenter=True, ycenter=True, font=None):
		self._text = str(text)
		if font == None:
			self._font = pygame.font.Font('data/Courier New.ttf', size) # fix later
		else:
			self._font = font
		self._screen = screen
		self._textsurf = self.font.render(self.text, True, color)
		self._textrect = self.textsurf.get_rect()
		self._textrect.center = (windowsize[0]/2)*xcenter + xoffset, (windowsize[1]/2)*ycenter + yoffset
	
	def display(self):
		self._screen.blit(self.textsurf, self.textrect)


	#### [ GET ] ####
	def get_text(self):
		return self._text

	def get_screen(self):
		return self._screen

	#### [ SET ] ####
	def set_text(self, text):
		self._text = text

	def set_screen(self, screen):
		self._screen = screen


def xbutton():
	

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