import json
import time
from datetime import datetime

import requests


#
# from reach_api.models import WbMessage


class JsonWriterPipeline(object):
    """
    写入json文件的pipline
    """

    def __init__(self):
        self.file = None
        # if not os.path.exists('../output'):
        #     os.mkdir('../output')

    # def process_item(self, item, spider):
    #     """
    #     处理item
    #     """
    #     if not self.file:
    #         now = datetime.datetime.now()
    #         file_name = spider.name + "_" + now.strftime("%Y%m%d%H%M%S") + '.jsonl'
    #         self.file = open(f'../output/{file_name}', 'wt', encoding='utf-8')
    #     item['crawl_time'] = int(time.time())
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     self.file.flush()
    #     return item

    def process_item(self, item, spider):
        item['crawl_time'] = int(time.time())
        # wb = WbMessage()
        # wb.content = item['content']
        # wb.consumed = False
        # wb.createdAt = datetime.now()
        # wb.updatedAt = datetime.now()
        # wb.save()
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # spider.logger.info(f'spider get new info: {line}')
        url = 'http://localhost:80/api/message/add'
        data = {
            'content': item['content']
        }

        requests.post(url, json=data)
        return item
