# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)

    def __init__(self, name, industry, area, pb, pe):
        self.name = name
        self.industry = industry
        self.area = area
        self.pb = pb
        self.pe = pe
