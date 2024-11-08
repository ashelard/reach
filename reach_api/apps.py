import logging
import os

from django.apps import AppConfig

import reach_api.schedule.scheduler


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reach_api'
    logger = logging.getLogger('log')
    ready_run = False

    def ready(self):
        reach_api.schedule.scheduler.start_scheduler()
