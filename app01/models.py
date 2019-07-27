from django.db import models
import datetime


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    vip = models.BooleanField(default=False)
    balance = models.FloatField(default=0)
    utype_choices = (
        (0, '普通用户'),
        (1, '管理员')
    )
    utype = models.IntegerField(choices=utype_choices, default=0)  # 0为普通用户
    islock = models.BooleanField(default=False)


class History(models.Model):
    id = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=32)
    down_time = models.DateTimeField('下载日期', default=datetime.datetime.now())
    uid = models.ForeignKey(to='User')


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=164)
    pub_time = models.DateTimeField('发布日期', default=datetime.datetime.now())
    uid = models.ForeignKey(to='User')


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    path = models.CharField(max_length=300)
    up_time = models.DateTimeField('上传日期', default=datetime.datetime.now())
    # uid = models.ForeignKey(to='User')
    is_free_choice = (
        (0, '收费'),
        (1, '免费')
    )
    is_free = models.IntegerField(choices=is_free_choice, default=1)  # 1 免费
