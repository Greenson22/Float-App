from .animals.animal import Animal
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import QTimer

import random

class Word(Animal):
     def __init__(self, window, random_spawn=True):
          super().__init__(window)
          self.window = window
          self.life_time = QTimer(self)
          self.life_time.timeout.connect(self.explotion)
          self.life_time.start(random.randint(5000, 15000))

          self.setText(kata_positif[random.randint(0, len(kata_positif)-1)])
          
          if random_spawn:self.random_spawn()
          
          self.setPalette(self.get_palette())
          self.setFont(self.get_font())
     
     def explotion(self):
          word = Word(self.window, random_spawn=False)
          word.move(self.x(), self.y())
          word.show()
          # for i in range(len(self.window.objects)):
          #      if self.window.objects[i] == self:
          #           print("helo ada reen ")
          #           self.window.objects.pop(i)
          self.deleteLater()

     def process(self):
          super().move_to_target()

     def get_palette(self):
          palette = QPalette()
          palette.setColor(QPalette.WindowText, QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
          return palette
     
     def get_font(self):
          font_list = ['Broadway', 'Times New Roman', 'Bauhaus 93', 'Felix Titling']

          font = QFont()
          font.setFamily(font_list[random.randint(0, len(font_list)-1)])
          font.setPointSize(random.randint(12, 16))
          font.setBold(random.randint(0, 1))
          font.setItalic(random.randint(0, 1))
          return font
     
kata_positif = [
     'hello'
]