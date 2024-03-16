import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(30),
                    age TINYINT,
                    password VARCHAR(30),
                    birthdate DATE,
                    place VARCHAR(10)
                )''')
connection.commit()
cursor.execute('''INSERT INTO users
                (username,age,password,birthdate,place) VALUES
                ("User1",20,"pass1","2000.12.12","Town1")
                ''')
connection.commit()