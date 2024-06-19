from creatures import Butterfly

class World:
	def __init__(self, window, objects):
		self.objects = objects
		[objects.append(Butterfly(window)) for _ in range(50)]

	def process(self):
		pass