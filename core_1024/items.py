# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Core1024Item(scrapy.Item):
    # define the fields for your item here like:
    page_url = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    av_girl = scrapy.Field()
    av_format = scrapy.Field()
    av_size = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    download_url = scrapy.Field()
    image_path = scrapy.Field()
