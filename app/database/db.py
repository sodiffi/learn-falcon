import psycopg2

import time

def test():
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
            curs.execute('SELECT * FROM "user" ')
            rows = curs.fetchone()
    conn.close()
    return rows
