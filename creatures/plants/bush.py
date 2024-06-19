from PyQt5.QtWidgets import QLabel
from .plant import Plant
from images.plant_sprite import BushSprite
import random

class Bush(Plant):
    def __init__(self, window):
        super().__init__(window)
        bush_type_list = list(BushSprite.TYPE)
        self.sprite = BushSprite().get_pixmap(bush_type_list[random.randint(0, len(bush_type_list)-1)])
        self.setPixmap(self.sprite)
        super().random_spawn()