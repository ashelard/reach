import logging
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from reach_api.wspider.spiders.comment import CommentSpider
from reach_api.wspider.spiders.fan import FanSpider
from reach_api.wspider.spiders.follower import FollowerSpider
from reach_api.wspider.spiders.repost import RepostSpider
from reach_api.wspider.spiders.tweet_by_keyword import TweetSpiderByKeyword
from reach_api.wspider.spiders.tweet_by_tweet_id import TweetSpiderByTweetID
from reach_api.wspider.spiders.tweet_by_user_id import TweetSpiderByUserID
from reach_api.wspider.spiders.user import UserSpider

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
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'comment': CommentSpider,
        'fan': FanSpider,
        'follow': FollowerSpider,
        'user': UserSpider,
        'repost': RepostSpider,
        'tweet_by_tweet_id': TweetSpiderByTweetID,
        'tweet_by_user_id': TweetSpiderByUserID,
        'tweet_by_keyword': TweetSpiderByKeyword,
    }
    process.crawl(mode_to_spider['tweet_by_user_id'])
    # the script will block here until the crawling is finished
    process.start()
