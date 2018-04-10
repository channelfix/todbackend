# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


# Create your models here.
class Room(models.Model):
    ROOM_STATUS = (
        (0, 'Inactive'),
        (1, 'Waiting for student'),
        (2, 'Ongoing'),
    )

    category = models.ForeignKey(Category, related_name='rooms')
    user_student = models.ForeignKey(User, related_name='rooms_student')
    user_tutor = models.ForeignKey(User, related_name='rooms_tutor')
    session_id = models.CharField(max_length=74, blank=True)
    status = models.PositiveIntegerField(choices=ROOM_STATUS,
                                         default=1)
