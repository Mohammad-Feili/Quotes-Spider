# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesSpiderItem(scrapy.Item):
    Text = scrapy.Field()
    Author = scrapy.Field()
    Tags = scrapy.Field()
