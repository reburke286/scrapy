# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

# simple version
import pymongo


class ReviewsPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['amazon']
        self.collection = db['reviews']

    def process_item(self, item, spider):
        valid = True

        if valid:
            self.collection.insert_one(dict(item))
        return item


class InfoPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['amazon']
        self.collection = db['prod_info']

    def process_item(self, item, spider):
        valid = True

        if valid:
            self.collection.insert_one(dict(item))
        return item


# complicated one
# from scrapy import settings
# from scrapy.exceptions import DropItem
#from scrapy import log


# class GoproProjectPipeline(object):

# def __init__(self, mongo_server, mongo_port, mongo_db):
#     self.mongo_server = mongo_server
#     self.mongo_port = mongo_port
#     self.mongo_db = mongo_db

# # @classmethod
# def from_crawler(cls, crawler):
#     settings = crawler.settings
#     collection = settings.get("COLLECTION NAME")
#     return cls(collection)
# def from_crawler(cls, crawler):
#     return cls(
# mongo_server=crawler.settings.get('MONGO_SERVER'),
# mongo_port=crawler.settings.get('MONGO_PORT'),
# mongo_db=crawler.settings.get('MONGO_DATABASE')
# )
# def open_spider(self, spider):
#     self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
#     print("Connection Established")
#     self.db = self.client[self.mongo_db]

# def close_spider(self, spider):
#     self.client.close()

# def process_item(self, item, spider):
#     db = self.connection['amazon']
#     self.collection = db[self.collection]
#     print("what even am i", self.collection)
#     valid = True
#     if valid:
#         self.collection.insert_one(dict(item))
#         print("Inserting into Database")
#         return item
