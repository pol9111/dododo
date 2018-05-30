import redis

r1 = redis.Redis(host='127.0.0.1', port='6379')
# 连接,给定参数ip/port， redis默认端口6379

r1.set('name', '徐鑫') # 设置键值对
str1 = r1.get('name')
print(str1.decode('utf-8')) # 解码


# 自动解码
r2 = redis.Redis(host='127.0.0.1', port='6379', decode_responses=True)
r2.set('name','哈哈')
str2 = r2.get('name')
print(str2)


# Redis和StrictRedis：Redis兼容旧版本python2
k_v = {
    'a1':'a',
    'a2':'b',
    'a3':'c'
}
r3 = redis.StrictRedis(host='127.0.0.1', port='6379')
r3.mset (**k_v) # 批量设置值
print(r3.mget('a1','a2','a3')) # 批量取值


r3.lpush('list1', 'haha') # 往列表添加值从头部开始
r3.lpush('list1', 3,4,5)
print(r3.lrange('list1',0,-1)) # 获取列表值

r3.sadd('set1', 'aa')
r3.sadd('set2', 'aa',8,10,'bb')
print(r3.smembers('set2'))






