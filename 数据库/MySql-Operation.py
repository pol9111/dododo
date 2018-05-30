import pymysql

db_config = {
    'host': '192.168.1.10',
    'user': 'admin',
    'password': 'Root110qwe',
    'db': 'homework1',
    'charset': 'utf8',
}


conn = pymysql.connect(**db_config)
try:
    cur = conn.cursor()
    rv = cur.execute('SELECT * FROM students;')
    res = cur.fetchall()
    print(rv)
    for entry in res:
        print(entry)

except:
    print('error')
    # conn.rollback()
finally:
    conn.commit()
    cur.close()
    conn.close()






