# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Opentok(models.Model):
    access_token = models.CharField(max_length=341)
    session_id = models.CharField(max_length=74)
    api_key = models.CharField(max_length=10)
