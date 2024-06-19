class FrameManager:
	def __init__(self):
		pass

	def get_frames(self, pixmap, row, col):
		size = (int(pixmap.width()/col), int(pixmap.height()/row))
		frames = []

		for i_row in range(row):
			frame_cols = []
			for i_col in range(col):
				frame_cols.append(pixmap.copy(i_col*size[0], i_row*size[1], size[0], size[1]))
			frames.append(frame_cols)
		return frames

