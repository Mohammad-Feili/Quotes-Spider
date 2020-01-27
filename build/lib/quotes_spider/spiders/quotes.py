# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(), response=response)

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath(
                './/*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()

            yield {'Text': text,
                   'Author': author,
                   'Tags': tags}

        # storing the scraped data into item files
        l.add_value('Text', text)
        l.add_value('Author', author)
        l.add_value('Tags', tags)

        l.load_item()

        next_page_url = response.xpath(
            '//*[@class="next"]/a/@href').extract_first()
        absolute_page_url = response.urljoin(next_page_url)
        yield Request(absolute_page_url)
