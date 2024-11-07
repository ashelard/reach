import datetime
import json
import logging
from http.cookies import SimpleCookie

import pytz
import requests
from scrapy import Spider
from scrapy.http import Request

from ..spiders.common import parse_tweet_info, parse_long_tweet, fill_tweet_origin, \
    simple_tweet, parse_long_retweet


class TweetSpiderByUserID(Spider):
    """
    用户推文数据采集
    """
    name = "tweet_spider_by_user_id"
    tz = pytz.timezone('Asia/Shanghai')

    def start_requests(self):
        """
        爬虫入口
        """
        # 这里user_ids可替换成实际待采集的数据
        user_ids = ['7716940453']
        # 这里的时间替换成实际需要的时间段，如果要采集用户全部推文 is_crawl_specific_time_span 设置为False
        is_crawl_specific_time_span = True
        start_time = self.tz.localize(datetime.datetime(year=2024, month=10, day=11))
        end_time = self.tz.localize(datetime.datetime(year=2024, month=10, day=12))
        cookies = self.get_cookies()

        for user_id in user_ids:
            url = f"https://weibo.com/ajax/statuses/searchProfile?uid={user_id}&page=1&hasori=1&hastext=1&haspic=1&hasvideo=1&hasmusic=1&hasret=1"
            if not is_crawl_specific_time_span:
                yield Request(url, cookies=cookies, callback=self.parse, meta={'user_id': user_id, 'page_num': 1})
            else:
                # 切分成10天进行
                tmp_start_time = start_time
                while tmp_start_time <= end_time:
                    tmp_end_time = tmp_start_time + datetime.timedelta(days=10)
                    tmp_end_time = min(tmp_end_time, end_time)
                    tmp_url = url + f'&starttime={int(tmp_start_time.timestamp())}&endtime={int(tmp_end_time.timestamp())}'
                    yield Request(tmp_url, cookies=cookies, callback=self.parse,
                                  meta={'user_id': user_id, 'page_num': 1})
                    tmp_start_time = tmp_end_time + datetime.timedelta(days=1)

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        data = json.loads(response.text)
        tweets = data['data']['list']
        for tweet in tweets:
            item = parse_tweet_info(tweet)
            if item['is_retweet']:
                if tweet.get('retweeted_status').get('isLongText', None):
                    url = "https://weibo.com/ajax/statuses/show?id=" + item['retweet_mblogid']
                    yield Request(url, callback=self.parse_single, meta={'origin': item})
                else:
                    retweet_item = parse_tweet_info(tweet['retweeted_status'])
                    fill_tweet_origin(retweet_item, item)
                    yield simple_tweet(retweet_item)
            elif item['isLongText']:
                url = "https://weibo.com/ajax/statuses/longtext?id=" + item['mblogid']
                yield Request(url, callback=parse_long_tweet, meta={'item': item})
            else:
                yield simple_tweet(item)
        if tweets:
            user_id, page_num = response.meta['user_id'], response.meta['page_num']
            url = response.url.replace(f'page={page_num}', f'page={page_num + 1}')
            yield Request(url, callback=self.parse, meta={'user_id': user_id, 'page_num': page_num + 1})

    def parse_single(self, response, **kwargs):
        data = json.loads(response.text)
        tweet = data
        item = parse_tweet_info(tweet)
        origin = response.meta['origin']
        if item['isLongText']:
            url = "https://weibo.com/ajax/statuses/longtext?id=" + item['mblogid']
            if origin:
                yield Request(url, callback=parse_long_retweet, meta={'item': item,'origin':origin})
            else:
                yield Request(url, callback=parse_long_tweet, meta={'item': item})

        if origin:
            item = fill_tweet_origin(item, origin)

        yield item

    def get_cookies(self):
        # auth = SpiderAuth.objects.get(name='initial_seven')
        # cookie_content = auth.cookie
        url = 'http://localhost:80/api/ruler/spider_auth/get_by_name?name=initial_seven'

        response = requests.get(url)
        js = response.json()
        if not js.get('data', {}).get('cookie', None):
            return None
        cookie_content = js.get('data').get('cookie')
        self.log(f"get cookie content from django{cookie_content}")
        cookie = SimpleCookie()
        cookie.load(cookie_content)
        cookies_dict = {key: morsel.value for key, morsel in cookie.items()}
        return cookies_dict

