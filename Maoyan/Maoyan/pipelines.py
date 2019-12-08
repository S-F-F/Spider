# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['star'],item['time'])
        return item
#存入到mysql数据库中
class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        self.mysql_db = pymysql.connect(host=MYSQL_HOST,
                                        user=MYSQL_USER,
                                        database=MYSQL_DB,
                                        password=MYSQL_PDW,
                                        charset=MYSQL_CHARSET,
                                        )
        self.cursor = self.mysql_db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        ins_list = [item['name'],item['star'],item['time']]
        self.cursor.execute(ins,ins_list)
        self.mysql_db.commit()
        return  item

    def close_spider(self,spider):
        self.mysql_db.close()
        self.cursor.close()

"""MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'maoyan'
MONGO_SET = 'maoyanset'"""
import pymongo
class MaoyanMongoPipeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(
            MONGO_HOST,MONGO_PORT
        )
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]
    def process_item(self,item,spider):
        info = dict(item)
        self.myset.insert(info)
        return item
