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


class Room(models.Model):
    student = models.ForeignKey(User, related_name='room_students')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='room_tutors')
    question = models.ForeignKey(Question, related_name='rooms')
    session_id = models.CharField(max_length=74)
    timestamp = models.DateTimeField(auto_now_add=True)


class RequestAnswer(models.Model):
    owner = models.ForeignKey(User, related_name='requestanswers')
    question = models.ForeignKey(Question, related_name='requestanswers')
    status = models.PositiveIntegerField(choices=QUESTION_STATUS,
                                         default=0)


class Opentok(models.Model):
    access_token = models.CharField(max_length=341)
    session_id = models.CharField(max_length=74)
    api_key = models.CharField(max_length=10)
