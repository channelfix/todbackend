# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.


class RequestPool(models.Model):
    STUDENT_STATUS = (
        (0, 'Inactive'),
        (1, 'Waiting'),
        (2, 'Pending'),
        (3, 'Ongoing'),
    )

    user = models.ForeignKey(User, related_name='request_pool')
    category = models.ForeignKey(Category, related_name='request_pool')
    status = models.PositiveIntegerField(choices=STUDENT_STATUS,
                                         default=0)
