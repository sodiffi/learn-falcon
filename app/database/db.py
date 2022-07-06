import psycopg2

import time




host = "ec2-3-222-24-200.compute-1.amazonaws.com"
dbname = "deasqmcplieukc"
user = "fdfqpstedohptf"
password = "3e0a3c171847dcf44c063091bd34377650779084d1e1f2d9805aba874469faee"
sslmode = "allow"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
with conn:
    with conn.cursor() as curs:
        start = time.time()
        curs.execute('SELECT * FROM user')
        rows = curs.fetchone()
        end = time.time()
        # Print all rows
        for row in rows:
            print(row)


conn.close()
        # Retrieve query results

print("The time used to execute this is given below")
print(end - start)




# import psycopg2

# # Update connection string information

# print("Connection established")
# cursor = conn.cursor()
# cursor = conn.cursor()
# # Fetch all rows from table
# cursor.execute("SELECT * FROM inventory;")
