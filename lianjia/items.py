# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
	link = scrapy.Field()
	img = scrapy.Field()
	title = scrapy.Field()
	position = scrapy.Field()
	floor = scrapy.Field()
	totlePrice = scrapy.Field()
	Price = scrapy.Field()

