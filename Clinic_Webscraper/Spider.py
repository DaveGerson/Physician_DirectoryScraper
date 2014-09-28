__author__ = 'gerson64'
import scrapy

class MySpider(scrapy.Spider):
    name = 'non_fellowship_SPIDER'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['www.mohssurgery.org/i4a/member_directory/feResultsListing.cfm?directory_id=3&bAdminPopup=0&viewAll=0']