import sqlite3
import os
import json
from .core import create_user_input

def create_db_table():
	try:
		db_path = os.path.join(os.path.dirname(__file__), "storage.db")
		connection = sqlite3.connect(db_path)
		cursor = connection.cursor()

		cursor.execute("""
					   CREATE TABLE IF NOT EXISTS user_inputs (
					   id INTEGER PRIMARY KEY AUTOINCREMENT,
				 	   date TEXT NOT NULL,
					   config TEXT,
					   text TEXT)
					   """)
		connection.commit()
		connection.close()

	except Exception as ex:
		print(ex)

def store_user_input(data):
	db_path = os.path.join(os.path.dirname(__file__), "storage.db")
	connection = sqlite3.connect(db_path)
	cursor = connection.cursor()

	cursor.execute("""
				   INSERT OR REPLACE INTO user_inputs (date, config, text)
				   VALUES (?, ?, ?)
				   """, (
					   data["date"],
					   json.dumps(data["config"]),
					   json.dumps(data["text"])
				   ))
	connection.commit()
	connection.close()

def load_user_inputs():
	db_path = os.path.join(os.path.dirname(__file__), "storage.db")
	connection = sqlite3.connect(db_path)
	cursor = connection.cursor()

	cursor.execute("SELECT date, config, text FROM user_inputs")
	rows = cursor.fetchall()

	for row in rows:
		date = row[0]
		config = json.loads(row[1])
		text = json.loads(row[2])
		create_user_input(date, text, config=None)
	
	connection.close()

def clear_user_input():
	db_path = os.path.join(os.path.dirname(__file__), "storage.db")
	connection = sqlite3.connect(db_path)
	cursor = connection.cursor()

	cursor.execute("DELETE FROM user_inputs")

	connection.commit()
	connection.close()

	print("DB has been cleared")

def delete_user_input(target_date, target_text):
	db_path = os.path.join(os.path.dirname(__file__), "storage.db")
	connection = sqlite3.connect(db_path)
	cursor = connection.cursor()

	json_text = json.dumps(target_text)

	cursor.execute("""
				   DELETE FROM user_inputs
				   WHERE date = ? AND text = ?
				   """, (target_date, json_text))
	
	connection.commit()
	connection.close()