import tkinter as tk
import config
from .core import delete_user_input

class EditWindow:
	def __init__(self, target_frame, date, text_memory):
		self.root = tk.Toplevel()
		self.root.geometry(config.CREATOR_WINDOW_SIZE)
		self.root.attributes("-topmost", True)

		self.target_frame = target_frame
		self.date = date
		self.text_memory = text_memory

	def create_edit_window(self):
		left_frame = tk.Frame(self.root, relief="solid", bd=1)
		left_frame.grid(row=0, column=0)
		right_frame = tk.Frame(self.root, relief="solid", bd=1)
		right_frame.grid(row=0, column=1)

		delete = tk.Button(left_frame, text="delete", command=self.delete_unser_input)
		delete.pack()
		edit = tk.Button(right_frame, text="edit")
		edit.pack()

	def delete_unser_input(self):
		delete_user_input(self.date, self.text_memory)
		self.target_frame.destroy()

	def run(self):
		self.root.mainloop()