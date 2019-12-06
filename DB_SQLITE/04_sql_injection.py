import sqlite3

conn = sqlite3.connect('users.db')

# cursor.execute('CREATE TABLE users (user_name TEXT,'
#                'user_password TEXT)')

users = [

     ('jack123', 'asdasdasd'),
     ('kasdsa', 'asdsadasd'),
     ('Bio', 'asdasda')
]


# insert_query = "INSERT INTO users VALUES (?, ?);"

user_name = input('Input user name: ')
user_password = input('Input you password: ')


# select_query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND " \
#     f"user_password = '{user_password}'"

# правильная запись запроса
select_query = f"SELECT * FROM users WHERE user_name = ? AND user_password = ?"

cursor = conn.cursor()
cursor.execute(select_query, (user_name, user_password))
data = cursor.fetchone()
if data:
    print('You are logged in!')
else:
    print("Please try again")
conn.commit()
conn.close()

# Итоговая строка выполнения запроса
# SELECT * FROM users WHERE user_name = '{user_name}' AND user_password = '' OR 1=1
# инъекция по парол
# ' or 1=1--'

# -- означает коментарий