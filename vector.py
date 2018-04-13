from math import *

def vector(m=None, r=None, x=None, y=None): # degrees
	assert (m is None and r is None) or (x is None and y is None), \
		'Only define magnitude and rotation or x and y components for a force vector.'
	if m is None and r is None:
		return _Vector(x=x, y=y)
	elif x is None and y is None:
		return _Vector(magnitude=m, rotation=r)
	else:
		assert 0, 'You should never see this. If you do...'

class _Vector:
	def __init__(self, magnitude=None, rotation=None, x=None, y=None):
		self.calc(self, magnitude, rotation, x, y)

	def calc(self, magnitude=None, rotation=None, x=None, y=None):
		assert (magnitude is None and rotation is None) or (x is None and y is None), \
			'Internal Error. _Vector class'

		if rotation is None and rotation is None:
			self.x = x
			self.y = y
			self.magnitude = sqrt(x**2 + y**2)
			self.rotation = degrees(atan(x/y))
			
		elif x is None and y is None:
			self.magnitude = magnitude
			self.rotation = rotation
			self.x = magnitude * cos(radians(rotation))
			self.y = magnitude * sin(radians(rotation))

		else:
			assert 0, 'You should never see this. If you do...'

	def __str__(self):
		return str([self.magnitude, self.rotation])