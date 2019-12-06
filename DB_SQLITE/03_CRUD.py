import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students;")

# for row in cursor:
#     print(row)

# print(cursor.fetchone()) # one row
# print(cursor.fetchall()) # all roe

cursor.execute("UPDATE students SET age = 18 WHERE first_name IS 'James' ")
cursor.execute("SELECT * FROM students;")
data = cursor.fetchall()
[print(row) for row in data]


conn.commit()
conn.close()
