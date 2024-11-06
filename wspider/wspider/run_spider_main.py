import logging
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from wspider.wspider.spiders.tweet_by_user_id import TweetSpiderByUserID

logger = logging.getLogger('log')

if __name__ == '__main__':
    logger.info("-------------start run spider main-----------------")
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'tweet_by_user_id': TweetSpiderByUserID,
    }
    process.crawl(mode_to_spider['tweet_by_user_id'])
    # the script will block here until the crawling is finished
    process.start()
