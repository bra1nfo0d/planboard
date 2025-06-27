import tkinter

def run_main_windows(weeks=2):
	from .gui import WhiteboardWindow
	main_window = WhiteboardWindow()	#creates the main window
	for i in range(weeks):				#creates the weeks in the main window
		main_window.week_layout(i)

	global date_frame_map
	date_frame_map = main_window.get_date_frame_map()

	main_window.run()					#runs the main window

def get_date_list(week=0):
	from .dates_times import get_date_str_list
	date_list = get_date_str_list(week)
	return date_list

def close_app(event, text="Manually closed. No Info given."):
	exit(text)

def on_enter_change_mouse(event, style="finger"):
	if style == "finger":
		event.widget.config(cursor="hand2")
	
def open_creator_window(event, date):
	from .gui_add import CreatorWindow
	creator_window = CreatorWindow(date)
	creator_window.creator_window_top()
	creator_window.run()

def create_user_input(date, text_memory, config=None):
	from .create_input import CreateInput
	newInput = CreateInput(date, text_memory, date_frame_map)
	newInput.build_input()
