from .animal import Animal
from images.animal_anim import WaspAnimPath
from PyQt5.QtGui import QMovie

class Wasp(Animal):
    def __init__(self, window):
        super().__init__(window)
        anim = WaspAnimPath().get_anim()
        self.set_movie(anim)
    
    def process(self):
        super().process()
        super().move_to_target()