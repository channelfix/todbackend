# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


# Create your models here.
class Tutor(models.Model):
    TUTOR_STATUS = (
        (0, 'Available'),
        (1, 'Unavailable'),
    )

    user = models.ForeignKey(User, related_name='tutors')
    category = models.ForeignKey(Category, related_name='tutors')
    create_time = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=TUTOR_STATUS,
                                         default=0)
