import logging

from django.apps import AppConfig

from reach_api.schedule.scheduler import start_scheduler


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reach_api'

    def ready(self):
        logging.info("---------ready runned---------------")
        start_scheduler()
