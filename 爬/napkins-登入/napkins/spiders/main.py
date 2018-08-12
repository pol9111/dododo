# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from napkins.items import NapkinsItem
from scrapy import FormRequest



class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['processon.com']
    start_urls = ['https://www.processon.com/login']

    def parse_start_url(self, response):
        # a = response.xpath('//form/input/@value[1]').extract_first()
        # print(a)
        formdate = {
           # 'csrfmiddlewaretoken': str(a),
           'login_email': 'biscuit36@163.com',
           'login_password': 'pr4%7ss416248MRTW',
           # 'remember': 'on',
           # 'next': '/',
        }

        return [FormRequest.from_response(response, formdata=formdate, callback=self.after_login)]

    def after_login(self, response):
        lnk = 'https://www.processon.com/diagrams'
        return scrapy.Request(lnk)

    rules = (
        Rule(LinkExtractor(allow=(r'',)),  callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.text)
        item = NapkinsItem()
        try:
            item['ss'] = response.xpath('//*[@id="user-logo"]/img/@src').extract_first()
            if item['ss']:
                print('在登入状态')
                yield item
        except:
            pass
