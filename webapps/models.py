# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Wordpress(models.Model):
    containerWordpress = models.BooleanField()
    wordpressUser = models.CharField(max_length=255, blank=False, null=False)
    wordpressPassword = models.CharField(max_length=255, blank=False, null=False)
    containerSql = models.BooleanField()
    sqlUser = models.CharField(max_length=255, blank=False, null=False)
    sqlPassword = models.CharField(max_length=255, blank=False, null=False)
    sqlRootPassword = models.CharField(max_length=255, blank=False, null=False)