# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FareItem(Item):
    # define the fields for your item here like:
    # name = Field()
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
	# last_updated = Field(serializer=str)
pass