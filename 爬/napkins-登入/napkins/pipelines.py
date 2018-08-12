# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NapkinsPipeline(object):
    def process_item(self, item, spider):
        # print(item['ss'])
        # print(item['url'])
        try:
            with open('dd.txt', 'a') as f:
                f.write(item['ss'])
                # f.write(item['url'])
        except:
            pass
        return item
