import tkinter as tk
import config
from .core import open_edit_window

class CreateInput:
	def __init__(self, date, text_memory, date_frame_map, config=None):
		self.master_frame = date_frame_map[date]
		self.date = date
		self.text_memory = text_memory
		self.config = config

		self.input_frame = tk.Frame(self.master_frame, relief="solid", bd=1)
		self.input_frame.pack(fill="both", pady=2.5)

		self.input_frame.bind("<Button-1>", lambda e: open_edit_window(self.input_frame, self.date, self.text_memory))
	
	def build_input(self):
		for i in range(len(self.text_memory)):
			self.create_section(i)

	def create_section(self, i):
		frame = tk.Frame(self.input_frame, relief="solid", bd=1)
		frame.pack(fill="x")
		frame.bind("<Button-1>", lambda e: open_edit_window(self.input_frame, self.date, self.text_memory))

		for j in range(len(self.text_memory[i])):
			if j == 0:
				label = tk.Label(frame, 
					 			 text=self.text_memory[i][j],
								 font=(config.INPUT_HEADER_FONT_FAMILIE,
			   						   config.INPUT_HEADER_FONT_SIZE,
									   config.INPUT_HEADER_FONT_STYLE))
				label.pack()
				label.bind("<Button-1>", lambda e: open_edit_window(self.input_frame, self.date, self.text_memory))
			else:
				label = tk.Label(frame, text=self.text_memory[i][j])
				label.pack()
				label.bind("<Button-1>", lambda e: open_edit_window(self.input_frame, self.date, self.text_memory))