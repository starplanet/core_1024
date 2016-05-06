# -*- coding: utf-8 -*-
import scrapy
from core_1024.items import Core1024Item
import re

class RideSpider(scrapy.Spider):
    name = 'ridespider'
    base_url = 'http://hk.1024cc.org/bbs/'
    start_urls = ['http://hk.1024cc.org/bbs/forum-22-1.html']

    def parse(self, response):
        url_selectors = response.xpath('//td[@class="f_title"]/a')
        for s in url_selectors:
            url = s.xpath('@href').extract()[0]
            if url.startswith('thread'):
                text = s.xpath('text()').extract()[0]
                print text
                yield scrapy.Request(self.base_url + url, callback=self.parse_pic, meta={'title': text})

        redirect_selectors = response.xpath('//a[@class="p_redirect"]')
        redirect_selector = None
        for r in redirect_selectors:
            if r.xpath('text()').extract()[0] == u'\u203a\u203a':
                redirect_selector = r
                break
        if redirect_selector:
            redirect_url = redirect_selector.xpath('@href').extract()[0]
            yield scrapy.Request(self.base_url + redirect_url, callback=self.parse)

    def parse_pic(self, response):
        title = response.meta['title']
        item = Core1024Item()
        item['image_path'] = 'ride'
        item['page_url'] = response.url
        item['title'] = title
        text = response.xpath('//form//table')[0].xpath('.//div[@class="t_msgfont"]').extract()[0]
        match = re.search(u'出演女優.*：(.*)<br>', text)
        if match:
            item['name'] = match.group(1)
        else:
            item['name'] = ''

        match = re.search(u'影片格式.*：(.*)<br>', text)
        if match:
            item['av_format'] = match.group(1)
        else:
            item['av_format'] = ''

        match = re.search(u'影片大小.*：(.*)<br>', text)
        if match:
            item['av_size'] = match.group(1)
        else:
            item['av_size'] = ''

        item['image_urls'] = re.findall(u'<img src="(\S+\.jpg)".*>', text)

        match = re.search(u'下載地址\s*：\s*<a href="(\S+)".*</a>', text)
        if match:
            item['download_url'] = match.group(1)
        else:
            match = re.search(u'種子下載地址.*：\s*<a href="(\S+)".*</a>', text)
            if match:
                item['download_url'] = match.group(1)
            else:
                item['download_url'] = ''

        yield item



