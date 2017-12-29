# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem

class LianjsSpider(scrapy.Spider):
	name = 'lianjia'
	offset = 1
	url = "https://cd.lianjia.com/ershoufang/pg"
	allowed_domains = ['cd.lianjia.com']
	start_urls = [url + str(offset) + "tt2/"]

	def parse(self, response):
		for each in response.xpath("//ul[@class='sellListContent']/li[@class='clear']"):
			#init the item modal
			item = LianjiaItem()
			try:
				item["link"] = each.xpath("./a[1]/@href").extract()[0]
				item["img"] = each.xpath("./a[1]/img/@data-original").extract()[0]
				item["title"] = each.xpath("./div[1]/div[@class='title']/a/text()").extract()[0]
				item["position"] = each.xpath("./div[1]/div[@class='address']/div[1]/a/text()").extract()[0]
				item["floor"] = each.xpath("./div[1]/div[@class='flood']/div[1]/text()").extract()[0]
				item["totlePrice"] = each.xpath("./div[1]/div[@class='priceInfo']/div[1]/span/text()").extract()[0]
				item["Price"] = each.xpath("./div[1]/div[@class='priceInfo']/div[2]/span/text()").extract()[0]
			except:
				item["link"] = ""
				item["title"] = ""
				item["position"] = ""
			yield item
		if self.offset < 73: 
			self.offset += 1
		else:
			raise "over spider"
		yield scrapy.Request(self.url+str(self.offset)+ "tt2/",callback = self.parse)
