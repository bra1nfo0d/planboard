from .core import run_main_windows, load_user_inputs, create_db_table

def run():
	create_db_table()
	run_main_windows(2)

if __name__ == "__main__":
	run()