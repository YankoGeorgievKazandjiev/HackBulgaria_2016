import os
import sqlite3

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DIR_PATH, "Cinema.db")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()
