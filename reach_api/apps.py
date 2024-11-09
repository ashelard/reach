import logging
import os

from django.apps import AppConfig


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reach_api'

    def ready(self):
        pass
        # reach_api.schedule.scheduler.start_scheduler()
