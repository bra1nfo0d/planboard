import tkinter

def run_main_windows(weeks=2):
	from .gui import WhiteboardWindow
	main_window = WhiteboardWindow()	#creates the main window
	for i in range(weeks):				#creates the weeks in the main window
		main_window.week_layout(i)

	global date_frame_map
	date_frame_map = main_window.get_date_frame_map()

	load_user_inputs()

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

def load_user_inputs():
	from .storage import load_user_inputs
	load_user_inputs()

def store_user_input(data):
	from .storage import store_user_input
	store_user_input(data)

def create_db_table():
	from .storage import create_db_table
	create_db_table()

def clear_db_table(event):
	from .storage import clear_user_input
	clear_user_input()

def delete_user_input(target_date, target_text):
	from .storage import delete_user_input
	delete_user_input(target_date, target_text)

def open_edit_window(target_frame, date, text_memory):
	from .edit_input import EditWindow
	newEditWindow = EditWindow(target_frame, date, text_memory)
	newEditWindow.create_edit_window()
	newEditWindow.run()