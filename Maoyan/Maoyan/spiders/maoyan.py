# -*- coding: utf-8 -*-
import scrapy

from ..items import MaoyanItem
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['moayan.com']
    # start_urls = ['https://maoyan.com/board/4']
    def start_requests(self):
        url = 'https://maoyan.com/board/4?offset={}'
        for i in range(0,91,10):
            yield scrapy.Request(
                url=url.format(str(i)),
                callback=self.parse
            )
    def parse(self, response):
        data_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        item = MaoyanItem()
        for i in data_list:
            item['name'] = i.xpath('./a/@title').get().strip()
            item['star'] = i.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = i.xpath('.//p[@class="releasetime"]/text()').get().strip()

            yield item
