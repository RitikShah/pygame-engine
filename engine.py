from abc import ABCMeta, abstractmethod
from keys import keys, key_none
from color import Color
from math import *
import pygame

class Engine:
	def __init__(self, world, title, fps=60):
		pygame.init()
		
		self._world = world
		Entity.set_world(world)
		Text.set_world(world)

		self._clock = pygame.time.Clock()
		self._game_display = pygame.display.set_mode((self._world.get_width(), self._world.get_height()))
		self.fps = fps
		pygame.display.set_caption(str(title))

	def start(self):
		running = True
		if __debug__:
			print('Game Boot')
		while running:
			exit_code = self.gameloop()
			if exit_code == 'quit':
				running = False

		if __debug__:
			print('Game Close')
		pygame.quit()
		quit()

	def gameloop(self):
		fps = self.fps
		while True:
			# x-button and event pump
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 'quit'

			exit_code = self._world.update()
			if not exit_code is None:
				return exit_code

			pygame.display.flip()
			self._clock.tick(fps)

	def set_fps(self, fps):
		self._fps = fps

	def get_fps(self):
		return self._fps

	def get_world(self):
		return self._world

class World:
	def __init__(self, width, height):
		self._window = (width, height)
		self._game_ticks = 0
		self._gravity = 1
		self._gravity_toggle = True

		# Contains all sprites
		self._all_sprites = pygame.sprite.Group()

	def update(self):
		self._game_ticks += 1
		self._all_sprites.update()
		self._pygame_keys = pygame.key.get_pressed()

	def reset(self):
		pass

	def key(self, k):
		if k == 'any' and not self._pygame_keys == key_none:
			return 1
		try:
			output = self._pygame_keys[keys[str(k)]]
			if __debug__ and not output == 0:
				print('Key Press Code: ' + str(output))
		except:
			assert 0, "Invalid Key - See valid-keys.txt"
			output = 0
		return output

	def get_ticks(self):
		return self._game_ticks

	def get_width(self):
		return self._window[0]

	def get_height(self):
		return self._window[1]

	def add_sprites(self, *sprites):
		for sprite in sprites:
			self._all_sprites.add(sprite)
			if __debug__:
				print('Sprite added: ' + sprite)
	
	def get_sprites(self):
		return self._all_sprites

	def wait_for_release(self):
		pygame.event.pump()
		key = pygame.key.get_pressed()
		while not key == key_none:
			pygame.event.pump()
			key = pygame.key.get_pressed()
			self.clock.tick(self.fps)

class Screen:
	def __init__(self):
		self._screen_list = {}
		self._text_list = {}

	def add_text(self, *args, **kwargs):
		for a in args:
			self._text_list[args.index(a)] = a
			if __debug__:
				print('Text (no ref) added: ' + a.get_text())
		for k,v in kwargs:
			self._text_list[k] = v
			if __debug__:
				print('Text (ref) added: ' + v.get_text())

	def add_screens(self, **kwargs):
		for k,v in kwargs:
			self._screen_list[k] = v

	def get_text(self, key):
		return self._text_list[key]

	def display(self):
		while text in _text_list:
			text.display()

	@classmethod
	def set_world(cls, world):
		cls._world = world

	@classmethod
	def get_world(cls):
		return cls._world

class Text:
	def __init__(self, screen, text, color=Color.white, size=20, xoffset=0, yoffset=0, xcenter=True, ycenter=True, font='data/Courier New.ttf'):
		self._text = str(text)
		self._color = color
		self._font = pygame.font.Font(font, size)
		self._screen = screen
		self._surf = self._font.render(self._text, True, color)
		self._rect = self._surf.get_rect()
		self._rect.center = (get_world().get_width()/2)*xcenter + xoffset, (get_world().get_height()/2)*ycenter + yoffset
	
	def display(self):
		self._screen.blit(self._surf, self._rect)

	def get_text(self):
		return self._text

	def get_screen(self):
		return self._screen

	def update_text(self, text):
		self._text = str(text)
		self._surf = self._font.render(self._text, True, self._color)
		self._rect = self._surf.get_rect()
		self._rect.center = (get_world().get_width()/2)*xcenter + xoffset, (get_world().get_height()/2)*ycenter + yoffset
	
	def set_screen(self, screen):
		self._screen = screen

	@classmethod
	def set_world(cls, world):
		cls._world = world

	@classmethod
	def get_world(cls):
		return cls._world

class Entity(pygame.sprite.Sprite, metaclass=ABCMeta):
	def __init__(self, position, size, velocity=(0,0), acceleration=(0,0), color=None):
		# Superclass constructor call
		super().__init__()

		self._size = list(size)
		self._acceleration = list(acceleration)
		self._velocity = list(velocity)
		self._position = list(position)
		self._angle = 0 # In Degrees (unused)

		if color == None:
			self._color = randcolor()
		else:
			self._color = color

		# Set the background color and set it to be transparent
		self.image = pygame.Surface([*self._size])
		self.image.fill(self._color)

		# Update rect to update entity
		self.rect = self.image.get_rect()

	def set_position(self, x=None, y=None):
		assert not (x is None and y is None), "Insert either x or y parameter"
		if not x is None:
			self._position[0] = x
		if not y is None:
			self._position[1] = y

	def set_velocity(self, x=None, y=None):
		assert not (x is None and y is None), "Insert either x or y parameter"
		if not x is None:
			self._velocity[0] = x
		if not y is None:
			self._velocity[1] = y

	def set_accerelation(self, x=None, y=None):
		assert not (x is None and y is None), "Insert either x or y parameter"
		if not x is None:
			self._acceleration[0] = x
		if not y is None:
			self._acceleration[1] = y

	def get_x(self):
		return self._position[0]

	def get_y(self):
		return self._position[1]

	@abstractmethod
	def update(self):
		self.rect.x = self.get_x()
		self.rect.y = self.get_y()

	@classmethod
	def set_world(cls, world):
		cls._world = world

	@classmethod
	def get_world(cls):
		return cls._world

class Static_Entity(Entity):
	def update(self):
		super().update()

class Moving_Entity(Entity):
	def __init__(self, position, size, velocity=(0,0), acceleration=(0,0), color=None, collision=True):
		assert type(collision) is bool
		self._collision = collision
		super().__init__()

	def update(self):
		self._velocity[0] += self._acceleration[0]
		self._velocity[1] += self._acceleration[1]

		self._position[0] += self._velocity[0]
		self._position[1] += self._velocity[1]
		super().update()

# Quick Test
if __name__ == '__main__':
	class My_World(World):
		def update(self):
			super().update()
			if self.key('any'):
				return 'quit'

	my_world = My_World(800, 600)

	engine = Engine(my_world, 'Test Game')
	engine.start()