from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.response import get_base_url
import re
import urlparse
from graduate.items import GraduateItem

class GraduateSpider(CrawlSpider):
    name = "graduate"
    allowed_domains = ["http://grs.zju.edu.cn"]
    start_urls = ["http://grs.zju.edu.cn/2013xw"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        links = hxs.select("//a/@href").extract()
        for link in links:
            item = GraduateItem()
            item['image_urls'] = [urlparse.urljoin(response.url,link)]
            items.append(item)
        return items
