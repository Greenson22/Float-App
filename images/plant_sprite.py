from enum import Enum
from PyQt5.QtGui import QPixmap

dir = "assets/sprites/Pixel Art Flower Pack/"

class BushSprite:
	class TYPE(Enum):
		GREEN = 'Bush 1 - GREEN'
		GREEN2 = 'Bush 1 - GREEN 2'
		RED = 'Bush 1 - RED'
		RED2 = 'Bush 1 - RED 2'
		TEAL = 'Bush 1 - TEAL'
		TEAL2 = 'Bush 1 - TEAL 2'
		TEAL3 = 'Bush 1 - TEAL 3'
		WARM_GREEN = 'Bush 1 - WARM GREEN'
		WARM_GREEN2 = 'Bush 1 - WARM GREEN 2'

	def get_pixmap(self, type):
		path = dir+'Bush 1/'+type.value+'.png'
		return QPixmap(path)