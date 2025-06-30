import tkinter as tk
from .dates_times import get_callender_week_str, get_date_str
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

		self.weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Sammstag", "Sonntag"]

	def week_layout(self, week=0, days=5):
		# main frame
		frame = tk.Frame(self.root)
		frame.pack(side="left", anchor="n", fill="both", expand=True)

		# enabels callender week visibility
		if config.SHOW_CALENDER_WEEK:
			callender_week = tk.Label(frame,
							 		  text=get_callender_week_str(week),
									  relief="solid", bd=1)
			callender_week.grid(row=0, column=0, columnspan=days, sticky="nsew")

		for i in range(days):
			if get_date_list(week)[i] == get_date_str(day=0):
				label = tk.Label(frame,
								text=f"{self.weekdays[i]}\n{get_date_list(week)[i]}",
								width=10,
								relief="solid", bd=1,
								bg=config.WEEKDAY_TD_COLOR,
								font=(config.WEEKDAYS_FONT_FAMILIE,
									  config.WEEKDAYS_FONT_SIZE,
									  config.WEEKDAYS_FONT_STYLE))
				input_frame = tk.LabelFrame(frame,
											relief="solid", bd=1,
											bg=config.COLUMN_TD_COLOR,
											padx=5, pady=2.5)
			else:
				label = tk.Label(frame,
								text=f"{self.weekdays[i]}\n{get_date_list(week)[i]}",
								width=10,
								relief="solid", bd=1,
								bg=config.WEEKDAYS_BG_COLORS[(i+week)%2],
								font=(config.WEEKDAYS_FONT_FAMILIE,
									  config.WEEKDAYS_FONT_SIZE,
									  config.WEEKDAYS_FONT_STYLE))
				input_frame = tk.LabelFrame(frame,
											relief="solid", bd=1,
											bg=config.COLUMN_BG_COLOR,
											padx=5, pady=2.5)
			label.grid(row=1, column=i, sticky="nsew")
			label.bind("<Enter>", on_enter_change_mouse)
			label.bind("<Button-1>", lambda e: open_creator_window(e, get_date_list(week)[i]))
			input_frame.grid(row=2, column=i, sticky="nsew")
			self.date_frame_map[get_date_list(week)[i]] = input_frame

		for j in range(days):
			frame.grid_columnconfigure(j, weight=1)
		frame.grid_rowconfigure(2, weight=1)


	def get_date_frame_map(self):
		return self.date_frame_map

	def run(self):
		self.root.mainloop()