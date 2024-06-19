from PyQt5.QtGui import QMovie
from .animal import Animal
from images.animal_anim import WhaleAnimPath

class Whale(Animal):
    def __init__(self, window):
        super().__init__(window)
        anim = WhaleAnimPath().get_anim()
        self.set_movie(anim)
    
    def process(self):
        super().process()
        super().move_to_target()