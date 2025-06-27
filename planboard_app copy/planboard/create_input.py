import tkinter as tk
import config

class CreateInput:
	def __init__(self, date, text_memory, date_frame_map):
		self.master_frame = date_frame_map[date]
		self.text_memory = text_memory

		self.input_frame = tk.Frame(self.master_frame, relief="solid", bd=1)
		self.input_frame.pack()
	
	def build_input(self):
		for i in range(len(self.text_memory)):
			self.create_section(i)

	def create_section(self, i):
		frame = tk.Frame(self.input_frame, relief="solid", bd=1)
		frame.pack()
		for j in range(len(self.text_memory[i])):
			if j == 0:
				label = tk.Label(frame, 
					 			 text=self.text_memory[i][j],
								 font=(config.INPUT_HEADER_FONT_FAMILIE,
			   						   config.INPUT_HEADER_FONT_SIZE,
									   config.INPUT_HEADER_FONT_STYLE))
				label.pack()
			else:
				label = tk.Label(frame, text=self.text_memory[i][j])
				label.pack()