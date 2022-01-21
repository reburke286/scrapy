# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class GoproProjectPipeline:
#     def process_item(self, item, spider):
#         return item
import pymongo

# from scrapy import settings
# from scrapy.exceptions import DropItem
#from scrapy import log


class GoproProjectPipeline(object):

    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.connection['amazon']
        self.collection = db['gopro']

    def process_item(self, item, spider):
        valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(item))
            # log.msg("Review added to MongoDB database!",
            #         level=log.DEBUG, spider=spider)
        return item
