from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from creatures import Wasp, Whale, Butterfly
from images.animal_anim import WhaleAnimPath

class MySystemTray(QSystemTrayIcon):
	def __init__(self, app, window, objects):
		super().__init__(QIcon(WhaleAnimPath().get_anim()['right']), app)
		self.setToolTip("Floating App")
		self.show()
		self.objects = objects
		self.window = window

		main_menu = QMenu()
		spawn_menu = QMenu('spawn', main_menu)
		destroy_menu = QMenu('destroy', main_menu)
		window_menu = QMenu('window menu', main_menu)

		main_menu.addMenu(spawn_menu)
		main_menu.addMenu(destroy_menu)
		main_menu.addMenu(window_menu)

		main_menu.addAction('exit').triggered.connect(app.quit)
		spawn_menu.addAction('wasp').triggered.connect(lambda: self.spawn(Wasp(self.window)))
		spawn_menu.addAction('whale').triggered.connect(lambda: self.spawn(Whale(self.window)))
		spawn_menu.addAction('butterfly').triggered.connect(lambda: self.spawn(Butterfly(self.window)))

		destroy_menu.addAction('destroy random').triggered.connect(self.destroy_random)
		destroy_menu.addAction('destroy all').triggered.connect(self.destroy_all)

		window_menu.addAction('make transparent').triggered.connect(self.window.make_transparent_frameless)
		window_menu.addAction('show window').triggered.connect(self.window.restore_window)

		self.setContextMenu(main_menu)

	# memunculkan objek
	def spawn(self, obj):
		self.objects.append(obj)
		obj.show()

	# menghancurkan objek random
	def destroy_random(self):
		if self.objects:
			obj = self.objects.pop()
			obj.deleteLater()
		else:
			print("Object telah kosong")

	# menghancurkan semua objek
	def destroy_all(self):
		for _ in range(len(self.objects)):
			obj = self.objects.pop()
			obj.deleteLater()
		print("menghancurkan semua object")