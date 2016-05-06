# -*- coding: utf-8 -*-

# Scrapy settings for core_1024 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'core_1024'

SPIDER_MODULES = ['core_1024.spiders']
NEWSPIDER_MODULE = 'core_1024.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'core_1024 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'core_1024.pipelines.Core1024Pipeline': 1}
IMAGES_STORE = 'images/'
# IMAGES_THUMBS = dict(small=(50, 50), big=(270, 270))
IMAGES_MIN_WIDTH = 200
IMAGES_MIN_HEIGHT = 200
