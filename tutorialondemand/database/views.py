# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Room, RequestAns, Opentok
from .serializers import QuestionSerializer, RoomSerializer, RequestAnsSerializer, OpentokSerializer
from rest_framework import viewsets


# Create your views here.
class QuestionList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
