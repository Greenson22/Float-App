from PyQt5.QtGui import QMovie
from enum import Enum
import random as r

dir = "assets/sprites/animals/"
path = {
	'left' : '',
	'right' : ''
}

class WaspAnimPath:
	def get_anim(self):
		my_path = path.copy()
		my_path['left'] = dir+'wasp/wasp_l'
		my_path['right'] = dir+'wasp/wasp_r'
		return my_path

class WhaleAnimPath:
	def get_anim(self):
		my_path = path.copy()
		my_path['left'] = dir+'whale/whale_l'
		my_path['right'] = dir+'whale/whale_r'
		return my_path

class ButterflyAnimPath:
	class TYPE(Enum):
		NORMAL = 'blue_butterfly'
		BLACK = 'black_butterfly'
		GREEN = 'green_butterfly'
		# BIG = 'big_butterfly'
	
	def get_random_anim(self):
		r_type = list(self.TYPE)[r.randint(0, len(self.TYPE)-1)]
		return self.get_anim(r_type)

	def get_anim(self, type=None):
		bf_dir = dir+'butterfly/'
		my_path = path.copy()
		match type:
			# case self.TYPE.BIG:
			# 	my_path['left'] = bf_dir+'butterfly_l'
			# 	my_path['right'] = bf_dir+'butterfly_r'
			case self.TYPE.BLACK:
				my_path['left'] = bf_dir+'black_butterfly_64_l'
				my_path['right'] = bf_dir+'black_butterfly_64_r'
			case self.TYPE.GREEN:
				my_path['left'] = bf_dir+'green_butterfly_64_l'
				my_path['right'] = bf_dir+'green_butterfly_64_r'
			case _:
				my_path['left'] = bf_dir+'butterfly_64_l'
				my_path['right'] = bf_dir+'butterfly_64_r'
		return my_path