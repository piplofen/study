import sqlite3
from sqlite3 import Error
import datetime

def connectionBD():
	global cur, conn
	conn = None
	try:
		conn = sqlite3.connect("DataBase.db")
		cur = conn.cursor()
		print(f"{datetime.datetime.now()} Подключение к базе данных прошло успешно!")

	except Error as e:
		print(f"{datetime.datetime.now()} Произошла ошибка '{e}'")


connectionBD()