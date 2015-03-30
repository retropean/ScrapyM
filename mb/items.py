from scrapy.item import Item, Field

class FareItem(Item):
	origlocation = Field()	
	origtime = Field()
	origcity = Field()
	destcity = Field()
	destlocation = Field()
	desttime = Field()
	duration = Field()
	fare = Field()
	timescraped = Field()
	datescraped = Field()
	urlscraped = Field()
	departuredate = Field()
pass