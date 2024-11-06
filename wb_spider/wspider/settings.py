# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reach_api.settings')
django.setup()

BOT_NAME = 'spider'

SPIDER_MODULES = ['wb_spider.wspider.spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
}

LOG_LEVEL = 'DEBUG'

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 100,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'wb_spider.wspider.pipelines.JsonWriterPipeline': 300,
}
