import pymysql

db_config = {
    'host': '192.168.1.10',
    'user': 'admin',
    'password': 'Root110qwe',
    'db': 'homework1',
    'charset': 'utf8',
}
# 数据库配置信息

conn = pymysql.connect(**db_config) # 连接数据库

try:
    cur = conn.cursor() # 建立游标
    rv = cur.execute('SELECT * FROM students;') # 执行内容
    res = cur.fetchall() # 获取结果
    print(rv)
    for entry in res:
        print(entry)

except Exception as e:
    print(e)
    # conn.rollback()
finally:
    conn.commit() # 提交数据
    cur.close() # 关闭游标
    conn.close() # 关闭连接






