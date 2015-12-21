ScrapyM
=======

This is a python script that crawls the MB website & grabs all fares for a given date.

To run, you will need to install Python, Scrapy and all  of its dependencies as mentioned in the <a href="http://doc.scrapy.org/en/latest/intro/install.html#intro-install">Scrapy Installation guide</a>.

To crawl and dump CSV with data, navigate to the root directory in the command line and run the following:

<code>scrapy crawl mb -o [filename].csv -t csv</code>

Or simply execute:

<code>mb/launch.bat</code>

The script will generate a .csv file in the root directory that will contain all of the scraped data.

Phantomjs can be used for headless testing by launching <code>phantomjs --webdriver=4444</code> after it is installed and located in <code>PATH</code>.
