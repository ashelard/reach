from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print("Job started")


def start_scheduler():
    print("schduler started")
    scheduler = BackgroundScheduler()
    scheduler.add_job(job,'interval',seconds=10)
    scheduler.start()