# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
QUESTION_STATUS = (
    ('0', 'answered'),
    ('1', 'unanswered'),
    ('2', 'pending'),
)


class Question(models.Model):
    user = models.ForeignKey(User)
    status = models.CharField(max_length=11, choices=QUESTION_STATUS,
                              default=1)
    text = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.text


class Room(models.Model):
    student = models.ForeignKey(User, related_name='room_student')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='room_tutor')
    question = models.ForeignKey(Question, related_name='room')
    session_id = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)


class RequestAns(models.Model):
    owner = models.ForeignKey(User, related_name='RequestAns')
    question = models.ForeignKey(Question, related_name='RequestAns')
    status = models.CharField(max_length=11, choices=QUESTION_STATUS,
                              default=1)


class Opentok(models.Model):
    access_token = models.CharField(max_length=1000)
    s_id = models.CharField(max_length=1000)

