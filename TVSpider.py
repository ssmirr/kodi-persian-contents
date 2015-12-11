from scrapy import Spider, Item, Field, Selector, Request


class Channel(Item):
    title = Field()
    video_url = Field()
    page_url = Field()
    img_url = Field()


class TVSpider(Spider):
    name, start_urls = 'ip_spider', ['http://iranproud.com/livetv']

    def parse_channel(self, response):
        hxs = Selector(response)
        item = response.meta['record']
        item['video_url'] = hxs.xpath("body//div[@id='divVideoHolder']/@videosrc").extract()[0]
        item["title"] = hxs.xpath("body//div[@id='divTitrGrid']/text()").extract()[0]

        return item

    def parse(self, response):
        hxs = Selector(response)

        for record in hxs.xpath("//li/a"):
            item = Channel()
            item["page_url"] = "http://iranproud.com%s" % record.xpath('@href').extract()[0]
            item["img_url"] = record.xpath('img/@src').extract()[0]

            request = Request(item['page_url'], callback=self.parse_channel)
            request.meta['record'] = item
            yield request
            