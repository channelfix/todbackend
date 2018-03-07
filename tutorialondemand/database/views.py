# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from database.models import Opentok, Question, RequestAnswer, Room
from database.serializers import OpentokSerializer, QuestionSerializer, RequestAnswerSerializer, RoomSerializer 
from database.utils import OpenTokResource


# Create your views here.
class QuestionList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SessionView(APIView):

    def get(self, request, format=None):
        opentok = OpenTokResource.get_client()
        session = opentok.create_session()
        token = opentok.generate_token(session.session_id)
        api_key = settings.APIKEY
        opentok = Opentok(
            access_token=token,
            session_id=session.session_id,
            api_key=api_key
        )
        opentok.save()

        serializer = OpentokSerializer(opentok)

        return Response(serializer.data)
