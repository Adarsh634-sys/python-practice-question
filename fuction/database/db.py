import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
cursor =conn.cursor()
query = "insert into users (name, age) values (%s, %s)"
data=[
    ("John", 30),
    ("Jane", 25),
    ("Mike", 35),
    ("Sara", 28),
    ("Tom", 40)
]
cursor.executemany(query, data)
conn.commit()
print(f"{cursor.rowcount} rows inserted.")
cursor.close()
conn.close()