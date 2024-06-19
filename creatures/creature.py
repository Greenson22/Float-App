from PyQt5.QtWidgets import QLabel
import random

class Creature(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.target = (0, 0)
        self.window_ = window
        self.window_.timer_process.timeout.connect(self.process)
            
    def process(self):
        pass

    def random_spawn(self):
        self.move(random.randint(0, 1366), random.randint(0, 738))