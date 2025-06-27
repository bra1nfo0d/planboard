import tkinter as tk
from .dates_times import get_date_str_list, get_callender_week_str
from .core import on_enter_change_mouse, open_creator_window, close_app, get_date_list, clear_db_table
import config

class WhiteboardWindow:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title(config.WINDOW_TITEL)
		self.root.attributes("-fullscreen", config.FULLSCREEN)

		# key binds for dev-mode
		if config.DEV_MODE:
			self.root.bind("<x>", lambda e: close_app(e, "closed with dev shortcut <x>"))
			self.root.bind("<c>", lambda e: clear_db_table(e))

		# global list of date and frame tuple
		self.date_frame_map = {}

	def week_layout(self, week=0):
		# main frame
		frame = tk.Frame(self.root)
		frame.pack(side="left", anchor="n", fill="both", expand=True)

		# enabels callender week visibility
		if config.SHOW_CALENDER_WEEK:
			callender_week = tk.Label(frame,
							 		  text=get_callender_week_str(week),
									  relief="solid", bd=1)
			callender_week.grid(row=0, column=0, columnspan=5, sticky="nsew")

		# head of the week tabel
		monday = tk.Label(frame,
						  text=f"Montag\n{get_date_list(week)[0]}",
						  width=10,
					      relief="solid", bd=1,
						  bg=config.WEEKDAYS_BG_COLORS[(0+week)%2],
						  font=(config.WEEKDAYS_FONT_FAMILIE,
			   					config.WEEKDAYS_FONT_SIZE,
								config.WEEKDAYS_FONT_STYLE))
		monday.grid(row=1, column=0, sticky="nsew")
		monday.bind("<Enter>", on_enter_change_mouse)
		monday.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[0]))
		tuesday = tk.Label(frame,
						   text=f"Dienstag\n{get_date_list(week)[1]}",
						   width=10,
						   relief="solid", bd=1,
						   bg=config.WEEKDAYS_BG_COLORS[(1+week)%2],
						   font=(config.WEEKDAYS_FONT_FAMILIE,
			   					 config.WEEKDAYS_FONT_SIZE,
							 	 config.WEEKDAYS_FONT_STYLE))
		tuesday.grid(row=1, column=1, sticky="nsew")
		tuesday.bind("<Enter>", on_enter_change_mouse)
		tuesday.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[1]))
		wednesday= tk.Label(frame,
							text=f"Mittwoch\n{get_date_list(week)[2]}",
							width=10,
							relief="solid", bd=1,
							bg=config.WEEKDAYS_BG_COLORS[(0+week)%2],
						    font=(config.WEEKDAYS_FONT_FAMILIE,
			   					  config.WEEKDAYS_FONT_SIZE,
								  config.WEEKDAYS_FONT_STYLE))
		wednesday.grid(row=1, column=2, sticky="nsew")
		wednesday.bind("<Enter>", on_enter_change_mouse)
		wednesday.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[2]))
		thursday = tk.Label(frame,
						   	text=f"Donnerstag\n{get_date_list(week)[3]}",
							width=10,
							relief="solid", bd=1,
							bg=config.WEEKDAYS_BG_COLORS[(1+week)%2],
						    font=(config.WEEKDAYS_FONT_FAMILIE,
			   					  config.WEEKDAYS_FONT_SIZE,
								  config.WEEKDAYS_FONT_STYLE))
		thursday.grid(row=1, column=3, sticky="nsew")
		thursday.bind("<Enter>", on_enter_change_mouse)
		thursday.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[3]))
		friday = tk.Label(frame,
						  text=f"Freitag\n{get_date_list(week)[4]}",
						  width=10,
						  relief="solid", bd=1,
						  bg=config.WEEKDAYS_BG_COLORS[(0+week)%2],
						  font=(config.WEEKDAYS_FONT_FAMILIE,
			   					config.WEEKDAYS_FONT_SIZE,
								config.WEEKDAYS_FONT_STYLE))
		friday.grid(row=1, column=4, sticky="nsew")
		friday.bind("<Enter>", on_enter_change_mouse)
		friday.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[4]))

		# streches the week elements over the fullscreen
		for i in range(5):
			frame.grid_columnconfigure(i, weight=1)

		# columns of the week tabel
		monday_frame = tk.LabelFrame(frame,
							   		 relief="solid", bd=1,
									 bg=config.COLUMN_BG_COLOR,
									 padx=5, pady=2.5)
		monday_frame.grid(row=2, column=0, sticky="nsew")
		self.date_frame_map[get_date_list(week)[0]] = monday_frame
		tuesday_frame = tk.LabelFrame(frame,
									  relief="solid", bd=1,
									  bg=config.COLUMN_BG_COLOR,
									  padx=5, pady=2.5)
		tuesday_frame.grid(row=2, column=1, sticky="nsew")
		self.date_frame_map[get_date_list(week)[1]] = tuesday_frame
		wednesday_frame = tk.LabelFrame(frame,
										relief="solid", bd=1,
										bg=config.COLUMN_BG_COLOR,
										padx=5, pady=2.5)
		wednesday_frame.grid(row=2, column=2, sticky="nsew")
		self.date_frame_map[get_date_list(week)[2]] = wednesday_frame
		thursday_frame = tk.LabelFrame(frame,
								 	   relief="solid", bd=1,
									   bg=config.COLUMN_BG_COLOR,
									   padx=5, pady=2.5)
		thursday_frame.grid(row=2, column=3, sticky="nsew")
		self.date_frame_map[get_date_list(week)[3]] = thursday_frame
		friday_frame = tk.LabelFrame(frame,
							   		 relief="solid", bd=1,
									 bg=config.COLUMN_BG_COLOR,
									 padx=5, pady=2.5)
		friday_frame.grid(row=2, column=4, sticky="nsew")
		self.date_frame_map[get_date_list(week)[4]] = friday_frame

		frame.grid_rowconfigure(2, weight=1)

	def get_date_frame_map(self):
		return self.date_frame_map

	def run(self):
		self.root.mainloop()