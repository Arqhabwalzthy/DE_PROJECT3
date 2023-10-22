import psycopg2
import csv

#connect to postgresgl
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")
cur = conn.cursor()

#create table
cur.execute("""
        CREATE TABLE IF NOT EXIST latihan_users(
        id serial PRIMARY KEY
        ,email text
        ,name text
        ,phone text
        ,postal_code text)
        """
)

with open('C:\Users\AZ\Documents\Project 3\source\users_w_postal_code.csv') as f :
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING' row)

conn.commit()

