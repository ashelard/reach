from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(auto_now=True)

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
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'spider_auth'


class WbMessage(models.Model):
    id = models.AutoField
    wid = models.BigIntegerField()
    mblogid = models.CharField(max_length=20)
    uid = models.BigIntegerField()
    nick_name = models.CharField(max_length=50)
    content = models.CharField(max_length=4096)
    url = models.CharField(max_length=512)
    publish_at = models.DateTimeField(default=datetime.now(), )
    verified = models.BooleanField(default=False)

    origin_wid = models.BigIntegerField()
    origin_xid = models.CharField(max_length=20)
    origin_uid = models.BigIntegerField()
    origin_nick_name = models.CharField(max_length=50)

    consumed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'wb_message'
