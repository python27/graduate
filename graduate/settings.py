# Scrapy settings for graduate project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'graduate'

SPIDER_MODULES = ['graduate.spiders']
NEWSPIDER_MODULE = 'graduate.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'graduate (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = './'
