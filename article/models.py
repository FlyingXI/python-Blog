# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class blogPost(models.Model):
    title = models.CharField('标题', max_length=20)
    content = models.TextField(help_text='博客内容')
    pub_time = models.DateTimeField('发布时间')

