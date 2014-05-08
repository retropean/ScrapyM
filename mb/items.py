# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FareItem(Item):
    # define the fields for your item here like:
    # name = Field()
	deplocation = Field()	
	deptime = Field()
	depcity = Field()
	arrcity = Field()
	arrlocation = Field()
	arrtime = Field()
	duration = Field()
	fare = Field()
	# last_updated = Field(serializer=str)
pass