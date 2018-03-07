# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
QUESTION_STATUS = (
    (0, 'Unanswered'),
    (1, 'Pending'),
    (2, 'Answered'),
)


class Question(models.Model):
    user = models.ForeignKey(User, related_name='questions')
    status = models.PositiveIntegerField(choices=QUESTION_STATUS,
                                         default=0)
    text = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.text
