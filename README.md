ScrapyM
=======

This is a python script that crawls the MB website & grabs all fares for a given date.

To run, you will need to install Python, Scrapy and all  of its dependencies as mentioned in the Scrapy documentation.

To select the dates to scrape, either use the StartURLGenerator.xlsx file and then copy into mb_spider.py, or simply find & replace the existing date in the URL with the desired date.

To crawl and dump CSV with data, navigate to the root directory in the command line and run the following:

scrapy crawl mb -o [filename].csv -t csv
