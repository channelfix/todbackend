# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Rating(models.Model):

    user = models.ForeignKey(User, related_name='rating')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    no_of_ratings = models.PositiveIntegerField(default=0)
