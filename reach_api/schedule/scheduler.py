import logging

from apscheduler.schedulers.background import BackgroundScheduler


def job():
    logging.info("----------------------------Job started-------------------------------")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=20)
    scheduler.start()
