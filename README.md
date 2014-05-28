ScrapyM
=======

ScrapyM
This is a python script that crawls the MB website & grabs all fares for a given date.

To run, you will need to install Python, Scrapy and all  of its dependencies as mentioned in the Scrapy documentation.

To crawl and dump CSV with data, navigate to the root directory in the command line and run the following:

scrapy crawl mb -o [filename].csv -t csv
