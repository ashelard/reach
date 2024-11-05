import logging
import os
import django
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from wb_spider.wspider.spiders.tweet_by_user_id import TweetSpiderByUserID

logger = logging.getLogger('log')

# if __name__ == '__main__':
#     mode = sys.argv[1]
#     os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)
#     mode_to_spider = {
#         'comment': CommentSpider,
#         'fan': FanSpider,
#         'follow': FollowerSpider,
#         'user': UserSpider,
#         'repost': RepostSpider,
#         'tweet_by_tweet_id': TweetSpiderByTweetID,
#         'tweet_by_user_id': TweetSpiderByUserID,
#         'tweet_by_keyword': TweetSpiderByKeyword,
#     }
#     process.crawl(mode_to_spider[mode])
#     # the script will block here until the crawling is finished
#     process.start()


def run():
    logger.info("-------------start run spider-----------------")
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'wb_spider.wspider.settings'
    settings = get_project_settings()

    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reach_api.settings')
    # django.setup()

    process = CrawlerProcess(settings)
    mode_to_spider = {
        'tweet_by_user_id': TweetSpiderByUserID,
    }
    process.crawl(mode_to_spider['tweet_by_user_id'])
    # the script will block here until the crawling is finished
    logger.info("-------------process start start-----------------")
    process.start()
    logger.info("-------------process start end-----------------")


# if __name__ == '__main__':
#     logger.info("-------------start run spider-----------------")
#     os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)
#     mode_to_spider = {
#         'tweet_by_user_id': TweetSpiderByUserID,
#     }
#     process.crawl(mode_to_spider['tweet_by_user_id'])
#     # the script will block here until the crawling is finished
#     process.start()
