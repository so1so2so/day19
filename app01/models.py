# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import paramiko
class business(models.Model):
    caption = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
class host(models.Model):
    # 创建用户名列，字符类型，指定长度
    nid = models.CharField(max_length=32,primary_key=True)
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    b = models.ForeignKey('business',to_field='id')
