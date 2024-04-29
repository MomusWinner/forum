from psycopg2 import connect

conn = connect(dbname="forum_db", host="127.0.0.1", password="123", port="5430", user="app")

cursor = conn.cursor()
cursor.execute('create schema forum')
conn.commit()