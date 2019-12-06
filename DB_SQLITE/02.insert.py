import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
# cursor.execute("INSERT INTO students VALUES ('James', 'Braun', 25);")

# insert_query = "INSERT INTO students VALUES ('James', 'Braun', 25);"

firts_name = 'Jho'
last_name = 'Bro'
age = 45

jane = ('Jane', 'Air', 18)
students = [
    ('Sdf', 'SDS', 18),
    ('Sdsd', 'SDS', 24),
    ('SdSD', 'SDS', 45)
]
# плохой подход sql injection опасность
# cursor.execute(f"INSERT INTO students VALUES ('{firts_name}', '{last_name}', {age});")

# хороший подход
insert_query = "INSERT INTO students VALUES (?, ?, ?);"
# cursor.execute(insert_query, (first_name, last_name, age))
# cursor.execute(insert_query, jane)  # может сразу использовать tuple

# for student in students:
#     cursor.execute(insert_query, student)

cursor.executemany(insert_query, students)


conn.commit()
conn.close()
