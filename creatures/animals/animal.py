from ..creature import Creature
from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from PyQt5.QtGui import QMovie

import math
import random
from enum import Enum

class Animal(Creature):
      class Side(Enum):
        LEFT = 0
        RIGHT = 1

      class ChangeSignals(QObject):
          side_changed = pyqtSignal()

      def __init__(self, window):
         super().__init__(window)
         self.change_signals = self.ChangeSignals()
         self.side = self.Side.LEFT
         self.time = 0
         self.slow = 1
         self.event_timer = QTimer(self)
         self.event_timer.timeout.connect(self.event_timer_timeout)
         self.event_timer.start(1)

      def set_movie(self, anim):
         self.movie_l = QMovie(anim['left'])
         self.movie_r = QMovie(anim['right'])

         self.setMovie(self.movie_l)
         self.movie_l.start()
         self.change_signals.side_changed.connect(self.change_side)

      def process(self):
         self.view_direction()
     
      def move_to(self, x, y):
         arah_x = x - self.x()
         arah_y = y - self.y()

         # Normalisasi vektor arah (agar panjangnya 1)
         panjang_vektor = math.sqrt(arah_x**2 + arah_y**2)
         if panjang_vektor != 0:
               arah_x /= panjang_vektor
               arah_y /= panjang_vektor
         
         # Perbarui posisi objek berdasarkan vektor arah dan kecepatan
         self.time += 1
         if self.time >= self.slow:
               self.time = 0
               self.move(self.x()+round(arah_x * 1), self.y()+round(arah_y * 1))
          
      def move_to_target(self):
         self.move_to(self.target[0], self.target[1])
     
      def event_timer_timeout(self):
         self.target = (random.randint(0, self.window_.width()), random.randint(0, self.window_.height()))
         time = random.randint(3000, 10000)
         self.event_timer.start(time)
         self.slow = random.randint(1, 10)
     
      def view_direction(self):
         if (self.x()-self.target[0]) > 0 and self.side != self.Side.LEFT:
            self.side = self.Side.LEFT
            self.change_signals.side_changed.emit()
         elif (self.x()-self.target[0]) < 0 and self.side != self.Side.RIGHT:
            self.side = self.Side.RIGHT
            self.change_signals.side_changed.emit()
         
      def change_side(self):
        if self.side == self.Side.LEFT:
            self.setMovie(self.movie_l)
            self.movie_l.start()
        elif self.side == self.Side.RIGHT:
            self.setMovie(self.movie_r)
            self.movie_r.start()