import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger('log')

def job():
    log.info("----------------------------Job started-------------------------------")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=30)
    scheduler.start()
    log.info("---------scheduler runned---------------")
