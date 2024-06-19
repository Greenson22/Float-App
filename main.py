from PyQt5.QtWidgets import QApplication
from core import Window, MySystemTray
from world import World

app = QApplication([])

objects = []
window = Window(objects)
world = World(window, objects)
MySystemTray(app, window, objects)

window.setup_window(world.process)
app.exec_()

# call rikal_env/scripts/activate