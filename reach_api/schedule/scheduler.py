from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print("Job started")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=20)
    scheduler.start()
