from enum import enum
import color
import world
import visuals

class Engine:
	def __init__(self, world):
		self.world = world

	def on_execute(self):
		running = True
		while running
			exit_code = gameloop()
			if gameloop() == 'quit':
				running = False

		pygame.quit()
		quit()

	def gameloop(self):
		while True:
			# x-button and event pump
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 'quit'
			world.update()

class World:
	def __init__(self, width, height):
		self._window = (width, height)
		self._tick = 0
		self._back = None

		# Contains all sprites
		self._all_sprites = pygame.sprite.Group()

	def update(self):
		tick += 1

	def add_sprites(self, *sprites):
		for sprite in sprites:
			self._all_sprites.add(sprite)

	def set_back(self, back):
		self._back = back

	def get_sprites(self):
		return self._all_sprites



class Menu:
	def __init__(self):


class _Screen:
	def __init__(self, mode, back_=None, next_=None):
		assert(mode == 'static' or mode == 'moving')
		self._mode = mode
		self._back = back_
		self._next = next_
		self._text_list = []

	def add_text(self, *args):
		while a in args:
			self._text_list.append(a)

	def display(self):
		while text in _text_list:
			text.display()

class Text:
	def __init__(self, screen, text, color=color.white, size=20, xoffset=0, yoffset=0, xcenter=True, ycenter=True, font=None):
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