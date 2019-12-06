import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE Students (first_name TEXT,'
               'last_name TEXT, age INTEGER)')
conn.commit()

conn.close()
