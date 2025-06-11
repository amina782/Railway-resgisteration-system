import sqlite3
conn = sqlite3.connect("demo.db")
print("opened database successfully")
conn.execute("CREATE TABLE registerss (username varchar,email varchar,password varchar)")
print("table created successfully")
conn.close()
