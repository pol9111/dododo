# -*- coding: utf-8 -*-

import pymongo

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.MONGO_TABLE].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()



import sqlite3

class SQLitePipeline(object):

    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'scrapy_defaut.db')
        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
        item['upc'],
         item['name'],
        item['price'],
        item['review_rating'],
        item['review_num'],
        item['stock'],
        )
        sql = 'INSERT INTO books VALUES (?,?,?,?,?,?)'
        self.db_cur.execute(sql, values)
        # 每插入一条就commit一次会影响效率
        # self.db_conn.commit()







