# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from questions.models import Question
from questions.serializers import QuestionSerializer
from rest_framework import viewsets


# Create your views here.
class QuestionList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
