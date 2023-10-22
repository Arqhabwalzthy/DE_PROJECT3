import psycopg2

#connect to postgresgl
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")
cur = conn.cursor()


cur.execute("""
        CREATE TABLE IF NOT EXIST users_using_copy(
        id serial PRIMARY KEY
        ,email text
        ,name text
        ,phone text
        ,postal_code text)
        """
)

with open('C:\Users\AZ\Documents\Project 3\source\users_w_postal_code.csv') as f :
    next(f)
    cur.copy_from(f,'users_using_copy', sep=',', columns=('email','name','phone','postal_code'))

conn.commit()

# cur.execute("""
#         SELECT * FROM users_using_copy
#         """
# )
# cur.fetchall
