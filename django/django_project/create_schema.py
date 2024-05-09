from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()

conn = connect(dbname=getenv('POSTGRES_DB'),
               host=getenv('POSTGRES_HOST'),
               password=getenv('POSTGRES_PASSWORD'),
               port=getenv('POSTGRES_PORT'),
               user=getenv('POSTGRES_USER'))

cursor = conn.cursor()
cursor.execute('create schema forum')
conn.commit()