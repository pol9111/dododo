import pymysql

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'qwe123',
    'db': 'homework3',
    'charset': 'utf8',
}

conn = pymysql.connect(**db_config)

try:
    cur = conn.cursor()
    id = '2018002'
    name = 'lelei'
    age = 18
    table = 'students'
    condition = 'age > 20'
    # sql = "CREATE TABLE students(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))"
    # sql = 'select * from student;'
    # sql = 'delete from {table} WHERE {condition}'.format(table=table, condition=condition)
    sql = 'INSERT INTO students(id. name. age) VALUES(%s,%s,%s)'
    exe = cur.execute(sql)
    exe1 = cur.execute(sql, (id, name, age))
    result = cur.fetchall()
    print(exe)
    for item in result:
        print(item)


except Exception as e:
    print(e)

finally:
    conn.commit()
    cur.close()
    conn.close()













