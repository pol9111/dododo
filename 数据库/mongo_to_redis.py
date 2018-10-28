import pymongo
import redis

mongo_client = pymongo.MongoClient('127.0.0.1', 27017)
db = mongo_client['baidu']
table = db['tiezi']

redis_client = redis.Redis(host='127.0.0.1', port=6379, db=2, decode_responses=True)


for i in range(0, 50001, 10000):
    data = table.find().skip(i).limit(i+10000)
    print(i)
    for j in data:
        j.pop('_id')
        redis_client.sadd('tiezi', j)

print('finish')


















