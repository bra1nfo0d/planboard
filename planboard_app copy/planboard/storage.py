import sqlite3
import json
import os
import config

def store_input_data(data):
	try:
		# creates db file in the current directory of the programm
		db_path = os.path.join(os.path.dirname(__file__), "storage.db")
		connection = sqlite3.connect(db_path)
		cursor = connection.cursor()

		# creates db structur if not already created
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS input_data (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			data TEXT NOT NULL
			)
			""")

		# inputs data into db
		cursor.execute("INSERT INTO input_data (data) VALUES (?)", (json.dumps(data),))
		connection.commit()

		load_input_data()

		connection.close()

	except Exception as ex:
		print(ex)

def load_input_data():
	from .create_input import CreateInput
	# creates db file in the current directory of the programm
	db_path = os.path.join(os.path.dirname(__file__), "storage.db")
	connection = sqlite3.connect(db_path)
	cursor = connection.cursor()

	cursor.execute("SELECT data FROM input_data")

	for row in cursor.fetchall():
		json_data = row[0]
		data = json.loads(json_data)

		print(data)

def delete_data():
	if config.DELETE_DATA_BY_CLOSING == True:
		db_path = os.path.join(os.path.dirname(__file__), "storage.db")
		connection = sqlite3.connect(db_path)
		cursor = connection.cursor()

		cursor.execute("DROP TABLE IF EXISTS input_data")

		connection.commit()
		connection.close()