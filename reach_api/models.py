from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(), )

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'Counters'  # 数据库表名


class SpiderAuth(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=128)
    wid = models.BigIntegerField()
    cookie = models.CharField(max_length=2048)
    expired = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(), )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'spider_auth'


# class WbMessage(models.Model):
#     id = models.AutoField
#     wid = models.BigIntegerField()
#     wuid = models.BigIntegerField()
#     content = models.CharField(max_length=2048)
#     consumed = models.BooleanField(default=False)
#     publishAt = models.DateTimeField(default=datetime.now(), )
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(), )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'wb_message'
