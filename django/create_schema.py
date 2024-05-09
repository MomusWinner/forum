from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()

conn = connect(dbname=getenv('PG_DBNAME'),
               host=getenv('PG_HOST'),
               password=getenv('PG_PASSWORD'),
               port=getenv('PG_PORT'),
               user=getenv('PG_USER'))

cursor = conn.cursor()
cursor.execute('create schema forum')
conn.commit()