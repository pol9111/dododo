import pymysql

db_config = {
    'user':'admin',
    'password':'Root110qwe',
    'db':'homework',
    'charset':'utf8'
}


def get_page(n, m):
    try:
        cur = conn.cursor() #设置控制的光标
        sql = 'SELECT * FROM students LIMIT %s, %s' % ((n-1)*m, n) #查询某表所有信息限制页数
        cur.execute(sql) #操作光标去执行
        for i in cur.fetchall(): #循环显示获得结果
            print(i)
    except Exception as e:
        print(e)
    finally:
        cur.close() #关闭光标


try:
    conn = pymysql.connect(**db_config) #连接数据库
    while True:
        n = input('请输入页码：')
        if n == 'q': #quit
            break
        elif n.isdigit(): #判断是否是数字
            get_page(int(n), 3) #执行函数
        else:
            print('无效输入！！！')

except Exception as e:
    print(e)
finally:
    conn.close() #关闭连接




