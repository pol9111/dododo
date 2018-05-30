from pymongo import *

client = MongoClient('127.0.0.1', 27017) # 建立连接
db = client.Trleo1 # 指定数据库
collection = db.col # 指定集合
# print(collection)

mydict ={
    '_id': 6,
    'name': 'zhanglinlin',
    'age': 18,
    'addr': 'didu'
}


# collection.insert(mydict)
print(collection.find())
for i in collection.find():
    print(i)
for i in collection.find({'name':'zhanglinlin'}):
    print(i)


