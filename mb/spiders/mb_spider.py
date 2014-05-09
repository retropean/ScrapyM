from scrapy.spider import Spider
from scrapy.selector import Selector

from mb.items import FareItem

class MBSpider(Spider):
	name = "mb"
	download_delay = 5
	allowed_domains = ["megabus.com"]
	start_urls = ["http://us.megabus.com/JourneyResults.aspx?originCode=142&destinationCode=143&outboundDepartureDate=5%2f16%2f2014&inboundDepartureDate=&passengerCount=1&transportType=0&concessionCount=0&nusCount=0&outboundWheelchairSeated=0&outboundOtherDisabilityCount=0&inboundWheelchairSeated=0&inboundOtherDisabilityCount=0&outboundPcaCount=0&inboundPcaCount=0&promotionCode=&withReturn=0"]

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul[@class="journey standard none"]')
		items = []
		for site in sites:
			item = FareItem()
			item['depcity'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[3]').extract())
			item['deplocation'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[5]').extract())
			item['deptime'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[2][normalize-space()]').extract())
			item['arrcity'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[3]').extract())
			item['arrlocation'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[5]').extract())
			item['arrtime'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[2]').extract())
			item['duration'] = map(unicode.strip, site.xpath('.//li[@class="three"]/p/text()').extract())
			item['fare'] = map(unicode.strip, site.xpath('.//li[@class="five"]/p/text()[normalize-space()]').extract())
			items.append(item)
		return items