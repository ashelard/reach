import logging
import time

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management.base import BaseCommand

log = logging.getLogger('log')


class Command(BaseCommand):
    help = 'Start a periodic task'

    def handle(self, *args, **options):
        self.start_task()
        while True:
            time.sleep(5)


    def start_task(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.job, 'interval', seconds=30)
        scheduler.start()
        log.info("---------scheduler runned---------------")


    def job(self):
        log.info("----------------------------Job started-------------------------------")
        url = 'http://localhost:80/test/job'
        requests.get(url)
