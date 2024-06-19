from ..creature import Creature

class Plant(Creature):
     def __init__(self, window):
          super().__init__(window)
     
     def process(self):
          super().process()