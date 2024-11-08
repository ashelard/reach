import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models.signals import post_migrate
from django.dispatch import receiver

log = logging.getLogger('log')

def job():
    log.info("----------------------------Job started-------------------------------")


@receiver(post_migrate)
def start_scheduler(sender, **kwargs):
    if sender.name == 'reach_api':
        scheduler = BackgroundScheduler()
        scheduler.add_job(job, 'interval', seconds=30)
        scheduler.start()
        log.info("---------scheduler runned---------------")
