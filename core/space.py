from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self, objects):
        super().__init__()
        self.timer_process = QTimer(self)
        self.timer_process.start(1)
        self.objects = objects
        self.move_to_screen2()

    # memindahkan ke screen 2
    def move_to_screen2(self):
        desktop = QDesktopWidget()
        amount_screen = desktop.screenCount()
        if amount_screen > 1:
            screen2 = desktop.screenGeometry(1)
            self.move(screen2.left(), screen2.top())

    # membuat window transparent
    def make_transparent_frameless(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    # mengembalikan window ke tidak transparent
    def restore_window(self):
        self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.show()

    # setup untuk window
    def setup_window(self, process):
        self.timer_process.timeout.connect(process)
        self.make_transparent_frameless()
        self.showMaximized()