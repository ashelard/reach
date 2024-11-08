import logging

from django.apps import AppConfig

from reach_api.schedule.scheduler import start_scheduler


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reach_api'
    logger = logging.getLogger('log')

    def ready(self):
        try:
            self.logger.info("Ready method called.")
            # 你的初始化代码
        except Exception as e:
            self.logger.error("Error in ready method: %s", e)

        start_scheduler()
