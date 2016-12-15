import scrapy
import datetime
import time
from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import date, time
from mb.items import FareItem

class MBSpider(Spider):
	custom_settings = {
		"DOWNLOAD_DELAY": 5.0,
		"RETRY_ENABLED": True,
	}
	name = "mb"
	allowed_domains = ["megabus.com"]
	urls = []

	def __init__(self, daysoutcmmd=0, *args, **kwargs):
		self.daysout = daysoutcmmd
		now = datetime.datetime.now() + datetime.timedelta(int(self.daysout))
		self.readyear = now.year
		self.readday = now.day
		self.readmonth = now.month
	
	def start_requests(self):
		locations = (
			[142, 143], [142, 289], [142, 94], [142, 95], [142, 99], [142, 101],
			[142, 131], [142, 110], [142, 118], [142, 299], [142, 5], [142, 389],
			[142, 127], [142, 132], [142, 135], [142, 145], [89, 123], [89, 133],
			[90, 96], [90, 112], [90, 123], [91, 100], [302, 289], [302, 454],
			[302, 131], [302, 455], [289, 302], [289, 292], [289, 95], [289, 99],
			[289, 290], [289, 100], [289, 101], [289, 102], [289, 103], [289, 454],
			[289, 105], [289, 131], [289, 108], [289, 455], [289, 296],	[289, 115],
			[289, 295],	[289, 118],	[289, 408],	[289, 298],	[289, 120],	[289, 294],
			[289, 293],	[289, 291],	[289, 303],	[289, 123],	[289, 297],	[289, 142],
			[320, 317],	[320, 318],	[320, 321],	[143, 94],	[143, 95],	[143, 110],
			[143, 123],	[143, 389],	[143, 127],	[143, 132],	[143, 135],	[143, 145],
			[143, 142],	[319, 317],	[319, 321],	[319, 303],	[93, 123],	[292, 289],
			[292, 100],	[292, 120],	[94, 143],	[94, 96],	[94, 112],	[94, 122],
			[94, 123],	[94, 127],	[94, 129],	[94, 135],	[94, 142],	[273, 123],
			[273, 134],	[273, 139],	[273, 145],	[95, 289],	[95, 143],	[95, 290],
			[95, 102],	[95, 103],	[95, 105],	[95, 108],	[95, 118],	[95, 408],
			[95, 123],	[95, 127],	[95, 134],	[95, 139],	[95, 145],	[95, 142],
			[420, 413],	[420, 414],	[420, 412],	[412, 420],	[412, 390],	[96, 90],
			[96, 94],	[96, 112],	[96, 123],	[96, 301],	[99, 289],	[99, 131],
			[99, 123],	[99, 132],	[99, 142],	[290, 302],	[290, 292],	[290, 95],
			[290, 99],	[290, 290],	[290, 100],	[290, 101],	[290, 102],	[290, 103],
			[290, 454],	[290, 105],	[290, 131],	[290, 108],	[290, 455],	[290, 296],
			[290, 115],	[290, 295],	[290, 118],	[290, 408],	[290, 298],	[290, 120],
			[290, 294],	[290, 293],	[290, 291],	[290, 303],	[290, 123],	[290, 297],
			[290, 142],	[290, 289],	[100, 91],	[100, 289],	[100, 292],	[100, 290],
			[100, 102],	[100, 103],	[100, 104],	[100, 105],	[100, 317],	[100, 106],
			[100, 107],	[100, 330],	[100, 331],	[100, 115],	[100, 116],	[100, 117],
			[100, 324],	[100, 298],	[100, 300],	[100, 119],	[100, 120],	[100, 121],
			[100, 144],	[100, 291],	[100, 123],	[100, 126],	[100, 136],	[100, 430],
			[100, 137],	[100, 140],	[101, 289],	[101, 118],	[101, 123],	[101, 142],
			[102, 289],	[102, 95],	[102, 290],	[102, 100],	[102, 103],	[102, 105],
			[102, 108],	[102, 115],	[102, 118],	[102, 408],	[103, 289],	[103, 95],
			[103, 137],	[103, 140],	[103, 290],	[103, 100],	[103, 103],	[103, 105],
			[103, 108],	[103, 115],	[103, 118],	[103, 408],	[104, 100],	[104, 117],
			[104, 136],	[454, 302],	[454, 289],	[454, 131],	[454, 455],	[105, 289],
			[105, 95],	[105, 290],	[105, 100],	[105, 102],	[105, 103],	[105, 108],
			[105, 115],	[105, 118],	[105, 408],	[317, 320],	[317, 98],	[317, 100],
			[317, 318],	[317, 324],	[317, 120],	[317, 321],	[317, 136],	[106, 100],
			[106, 116],	[106, 126],	[107, 100],	[107, 330],	[107, 331],	[131, 302],
			[131, 289],	[131, 99],	[131, 454],	[131, 455],	[131, 123],	[131, 132],
			[131, 142],	[330, 100],	[330, 107],	[330, 331],	[108, 289],	[108, 95],
			[108, 290],	[108, 102],	[108, 103],	[108, 105],	[108, 118],	[108, 408],
			[316, 123],	[316, 130],	[455, 302],	[455, 289],	[455, 454],	[455, 131],
			[296, 289],	[296, 294],	[296, 303],	[296, 297],	[296, 453],	[331, 100],
			[331, 107],	[331, 330],	[110, 143],	[110, 123],	[110, 389],	[110, 127],
			[110, 132],	[110, 142],	[111, 127],	[111, 128],	[111, 137],	[112, 90],
			[112, 94],	[112, 96],	[112, 122],	[112, 123],	[318, 320],	[318, 319],
			[318, 317],	[318, 303],	[318, 321],	[115, 289],	[115, 290],	[115, 100],
			[115, 102],	[115, 105],	[115, 298],	[115, 291],	[116, 100],	[116, 106],
			[116, 126],	[447, 120],	[447, 303],	[447, 446],	[295, 289],	[295, 297],
			[117, 100],	[117, 104],	[117, 136],	[118, 289],	[118, 95],	[118, 290],
			[118, 101],	[118, 102],	[118, 103],	[118, 105],	[118, 108],	[118, 408],
			[118, 123],	[118, 142],	[417, 390],	[417, 416],	[408, 302],	[408, 292],
			[408, 95],	[408, 99],	[408, 290],	[408, 100],	[408, 101],	[408, 102],
			[408, 103],	[408, 454],	[408, 105],	[408, 131],	[408, 108],	[408, 455],
			[408, 296],	[408, 115],	[408, 295],	[408, 118],	[408, 408],	[408, 298],
			[408, 120],	[408, 294],	[408, 293],	[408, 291],	[408, 303],	[408, 123],
			[408, 297],	[408, 142],	[408, 289],	[408, 290],	[324, 98],	[324, 100],
			[324, 317],	[324, 120],	[324, 136],	[390, 417],	[390, 413],	[390, 414],
			[390, 412],	[298, 289],	[298, 290],	[298, 100],	[298, 115],	[298, 291],
			[300, 100],	[300, 144],	[300, 430],	[119, 100],	[119, 144],	[119, 430],
			[120, 289],	[120, 292],	[120, 100],	[120, 317],	[120, 447],	[120, 324],
			[120, 303],	[120, 446],	[120, 136],	[450, 297],	[450, 451],	[121, 100],
			[121, 144],	[121, 430],	[144, 100],	[144, 300],	[144, 119],	[144, 121],
			[294, 289],	[294, 296],	[294, 293],	[294, 303],	[294, 297],	[294, 453],
			[293, 289],	[293, 294],	[293, 303],	[299, 128],	[299, 142],	[291, 289],
			[291, 290],	[291, 100],	[291, 115],	[291, 298],	[305, 123],	[122, 94],
			[122, 112],	[303, 289],	[303, 319],	[303, 296],	[303, 318],	[303, 447],
			[303, 120],	[303, 294],	[303, 293],	[303, 297],	[303, 446],	[303, 321],
			[303, 453],	[123, 89],	[123, 90],	[123, 289],	[123, 92],	[123, 143],
			[123, 93],	[123, 94],	[123, 273],	[123, 95],	[123, 96],	[123, 99],
			[123, 100],	[123, 101],	[123, 103],	[123, 131],	[123, 316],	[123, 110],
			[123, 112],	[123, 118],	[123, 305],	[123, 389],	[123, 127],	[123, 128],
			[123, 304],	[123, 130],	[123, 132],	[123, 134],	[123, 301],	[123, 137],
			[123, 139],	[123, 140],	[123, 145],	[123, 142],	[389, 143],	[389, 110],
			[389, 123],	[389, 127],	[389, 132],	[389, 142],	[413, 420],	[413, 390],
			[307, 306],	[306, 307],	[126, 100],	[126, 106],	[126, 116],	[297, 289],
			[297, 296],	[297, 295],	[297, 450],	[297, 294],	[297, 303],	[297, 453],
			[297, 451],	[446, 447], [446, 120],	[446, 303],	[127, 143],	[127, 94],
			[127, 95],	[127, 110],	[127, 111],	[127, 123],	[127, 389],	[127, 128],
			[127, 132],	[127, 135],	[127, 137],	[127, 145],	[127, 142],	[128, 111],
			[128, 299],	[128, 123],	[128, 127],	[128, 137],	[128, 142],	[129, 94],
			[304, 123],	[130, 316],	[130, 123],	[418, 415],	[418, 414],	[132, 143],
			[132, 99],  [132, 131],	[132, 110],	[132, 123],	[132, 389],	[132, 127],
			[132, 142],	[133, 89],	[416, 417],	[134, 273],	[134, 95],	[134, 123],
			[134, 139],	[134, 145],	[415, 418],	[415, 414],	[415, 419],	[321, 320],
			[321, 319],	[321, 317], [321, 318],	[321, 303], [414, 420],	[414, 390],
			[414, 418],	[414, 415],	[414, 419],	[412, 420],	[412, 390],	[301, 96],
			[301, 123],	[135, 143],	[135, 94],	[135, 127],	[135, 142],	[419, 415],
			[419, 414],	[136, 100],	[136, 104],	[136, 317],	[136, 117],	[136, 324],
			[136, 120],	[430, 100],	[430, 300],	[430, 119],	[430, 121],	[137, 100],
			[137, 103],	[137, 111],	[137, 123],	[137, 127],	[137, 128],	[137, 140],
			[139, 273],	[139, 95],	[139, 123],	[139, 134],	[139, 145],	[453, 296],
			[453, 294],	[453, 303],	[453, 297],	[451, 450],	[451, 297],	[140, 100],
			[140, 103],	[140, 123],	[140, 137],	[145, 143],	[145, 273],	[145, 95],
			[145, 123],	[145, 127],	[145, 134],	[145, 139],	[145, 142],	[457, 316],
			[457, 456], [457, 123], [456, 123], [456, 130], [462, 297], [462, 451],
			[297, 462], [451, 462], [466, 413], [413, 466], [466, 414], [466, 412],
			[414, 466], [412, 466])
		url_pattern = "http://us.megabus.com/JourneyResults.aspx?originCode={origin}&destinationCode={dest}&outboundDepartureDate={month}%2f{day}%2f{year}&inboundDepartureDate=&passengerCount=1&transportType=0&concessionCount=0&nusCount=0&outboundWheelchairSeated=0&outboundOtherDisabilityCount=0&inboundWheelchairSeated=0&inboundOtherDisabilityCount=0&outboundPcaCount=0&inboundPcaCount=0&promotionCode=&withReturn=0"

		for location in locations:
			self.urls.append(url_pattern.format(origin=location[0],dest=location[1], day=self.readday,month=self.readmonth, year=self.readyear))

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul[@class="journey standard none"]|//ul[@class="journey standard seat"]')
		items = []
		for site in sites:
			item = FareItem()
			item['origcity'] = str(map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[3]').extract())).split("[u'")[1].split("']")[0]
			item['origlocation'] = str(map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[5]').extract())).split("[u'")[1].split("']")[0]
			item['destcity'] = str(map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[3]').extract())).split("[u'")[1].split("']")[0]
			item['destlocation'] = str(map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[5]').extract())).split("[u'")[1].split("']")[0]
			item['timescraped'] = str(datetime.datetime.now().time())
			item['datescraped'] = str(datetime.datetime.now().date())
			item['fare'] = str(map(unicode.strip, site.xpath('.//li[@class="five"]/p/text()[normalize-space()]').extract())).split("[u'")[1].split("']")[0]
			
			#parse out departure date
			url = str(response.url)
			month = url[url.index('Date=')+5:url.index('%2f')]
			year = url[url.index('&in')-4:url.index('&in')]
			day = url[url.index('%2f')+3:url.index('%2f'+year)]
			year=int(year)
			day=int(day)
			month=int(month)
			item['departuredate'] = date(year, month, day)

			#fix origtime
			origintime = str(map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[2][normalize-space()]').extract())).split("[u'")[1].split("']")[0].replace('\\xa0', ' ')
			hour = origintime[0:origintime.index(':')]
			minutes = origintime[origintime.index(':')+1:origintime.index(':')+3]
			pmindicator = origintime[len(origintime)-2:len(origintime)]
			hour = int(hour)
			minutes = int(minutes)
			if pmindicator == "PM":
				if hour == 12:
					hour = 12
				else:
					hour = hour + 12
			if pmindicator == "AM":
				if hour == 12:
					hour = 0
			origintime = datetime.time(hour, minutes)
			item['origtime'] = origintime

			#fix desttime
			destinationtime = str(map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[2]').extract())).split("[u'")[1].split("']")[0].replace('\\xa0', ' ')
			hour = destinationtime[0:destinationtime.index(':')]
			minutes = destinationtime[destinationtime.index(':')+1:destinationtime.index(':')+3]
			pmindicator = destinationtime[len(destinationtime)-2:len(destinationtime)]
			hour = int(hour)
			minutes = int(minutes)
			if pmindicator == "PM":
				if hour == 12:
					hour = 12
				else:
					hour = hour + 12
			else:
				if hour == 12:
					hour = 0
			destinationtime = datetime.time(hour, minutes)
			item['desttime'] = destinationtime
			
			#fix duration
			durfix = str(map(unicode.strip, site.xpath('.//li[@class="three"]/p/text()').extract())).split("[u'")[1].split("']")[0]
			hour = durfix[0:durfix.index('hrs')]
			minutes = durfix[durfix.index('hrs')+4:durfix.index('mins')]
			hour = int(hour)
			minutes = int(minutes)
			durfix = datetime.timedelta(hours=hour, minutes=minutes)
			item['duration'] = durfix
			
			items.append(item)
		return items