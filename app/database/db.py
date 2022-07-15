import psycopg2

import time

from . import fordb

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
            f=curs.description
            rows = fordb("test",curs.fetchall(),f)
            
    conn.close()
    return rows

def insert(sql):
    host = "ec2-3-222-24-200.compute-1.amazonaws.com"
    dbname = "deasqmcplieukc"
    user = "fdfqpstedohptf"
    password = "3e0a3c171847dcf44c063091bd34377650779084d1e1f2d9805aba874469faee"
    sslmode = "allow"
    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    res="新增成功"
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql)
                conn.commit()
                curs.close()
                
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        res=error
    finally:
        conn.close()
    return res

