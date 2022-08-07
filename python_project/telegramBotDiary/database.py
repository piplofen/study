import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect("database.db", check_same_thread = False)
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name CHAR
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS diary(
                        id INTEGER,
                        data DATE,
                        text TEXT
                        )""")

except Error as er:
    print(er)