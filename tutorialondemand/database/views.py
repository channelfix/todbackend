# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Room, RequestAns, Opentok
from .serializers import QuestionSerializer, RoomSerializer, RequestAnsSerializer, OpentokSerializer
from rest_framework import viewsets
from opentok import OpenTok
from django.views import View
from django.http import HttpResponse
import json


# Create your views here.
APIKey = '46067082'
secretkey = 'ccbe3b20245ad940669e2d84248e311c6c5919ec'


class QuestionList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SessionView(View):

    def get(self, request, **kwargs):
        opentok = OpenTok(APIKey, secretkey)
        session = opentok.create_session()

        token = opentok.generate_token(session.session_id)
        opentokvar = Opentok(access_token=token,
                             s_id=session.session_id)
        print (token)

        opentokvar.save()

        context = Opentok.objects.all()
        context = context[0]
        x = {'access_token': context.access_token,
             's_id': context.s_id}

        return HttpResponse(json.dumps(x), 'text/json')
