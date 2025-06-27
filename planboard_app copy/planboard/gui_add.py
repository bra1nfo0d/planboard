import tkinter as tk
from .core import create_user_input
import config

# creates the input creator window
class CreatorWindow:
	def __init__(self, master_date):
		self.root = tk.Toplevel()										# window settings
		self.root.geometry(config.CREATOR_WINDOW_SIZE)
		self.root.attributes("-topmost", True)

		self.mainframe = tk.Frame(self.root, relief="solid", bd=1)		# main frame
		self.mainframe.pack()
		self.entryframe = tk.Frame(self.root, relief="solid", bd=1)		# entry frame
		self.entryframe.pack()

		self.master_date = master_date		# date where the input will be placed
		self.first_entrys = True			# satetment for checking if first user input

	def creator_window_top(self):
		date = tk.Label(self.mainframe,											# label wich displays the date
						text=self.master_date,
						relief="solid", bd=1,
						padx=30, pady=10)
		date.grid(row=0, column=0, sticky="nsew")
		drop_value = tk.StringVar(value=config.PRESET_LABEL_OPTIONS[0])			# dropbar, with the config options
		drop = tk.OptionMenu(self.mainframe,
							drop_value,
							*config.PRESET_LABEL_OPTIONS,
							command=lambda e: self.creator_window_bottom(drop_value.get()))
		drop.grid(row=0, column=1, sticky="nsew")

	def creator_window_bottom(self, drop_value):
		self.text_memory = []
		if self.first_entrys is True:											# change the bool state after opening first entrys
			self.first_entrys = False
		else:
			self.entryframe.destroy()											# destroys past entrys
			self.entryframe = tk.Frame(self.root, relief="solid", bd=1)
			self.entryframe.pack()

		for idx, header in enumerate(config.PRESET_LABEL_HEADERS[drop_value]):	# creates the amount of entrys and list to store text
			text_list = []
			self.text_memory.append(text_list)
			self.create_entry(header, idx)
		
		button = tk.Button(self.entryframe, text="Submit", command=lambda:self.submit_user_input(drop_value))
		button.grid(row=len(config.PRESET_LABEL_HEADERS[drop_value]), column=1)

	def create_entry(self, header, idx):
		label_list = []		# local list to store the created labels, to be able to delete them
		leftframe = tk.Frame(self.entryframe, relief="solid", bd=1)
		leftframe.grid(row=idx, column=0)
		rightframe = tk.Frame(self.entryframe, relief="solid", bd=1)
		rightframe.grid(row=idx, column=1)
		if header != "_":													# if text is not _ so is the first text from config
			self.text_memory[idx].append(header)							# added to the text memory
			label = tk.Label(leftframe, text=header)
			label.pack()
		entry = tk.Entry(rightframe)
		entry.pack()
		entry.bind("<Return>", lambda e: self.display_user_inputs(leftframe, entry.get(), entry, label_list, idx))
		entry.bind("<Delete>", lambda e: self.delete_user_input(label_list, idx))

	def display_user_inputs(self, frame, text, entry, label_list, idx):		# displays the user input
		label = tk.Label(frame, text=text)
		label.pack()
		label_list.append(label)
		self.text_memory[idx].append(text)
		entry.delete(0, tk.END)
	
	def delete_user_input(self, label_list, idx):							# deletes the user inputs
		try:
			label_list.pop().destroy()
			self.text_memory[idx].pop()
		except Exception as ex:
			print(ex)
	
	def submit_user_input(self, drop_value):							# submits the user input, wich get stored and
		create_user_input(self.master_date, self.text_memory)				# showscreened on the main window
		self.text_memory.clear()
		self.creator_window_bottom(drop_value)

	def run(self):															# runs the creator window
		self.root.mainloop()