from .animal import Animal
from images.animal_anim import ButterflyAnimPath

class Butterfly(Animal):
    def __init__(self, window):
        super().__init__(window)
        anim = ButterflyAnimPath().get_random_anim()
        self.set_movie(anim)
        self.random_spawn()
    
    def process(self):
        super().process()
        super().move_to_target()