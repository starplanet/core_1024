# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline


class Core1024Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = super(Core1024Pipeline, self).get_media_requests(item, info)
        if 'image_path' in item:
            info.image_path = item['image_path']
            print 'get_media_requests:', info
        return requests

    def file_path(self, request, response=None, info=None):
        path = super(Core1024Pipeline, self).file_path(request, response, info)
        print 'file_path:', info.image_path
        if hasattr(info, 'image_path'):
            path = info.image_path + '/' + path
        return path
