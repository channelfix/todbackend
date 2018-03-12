# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from rest_framework.response import Response
from livestream.models import Opentok
from livestream.serializers import OpentokSerializer
from livestream.utils import OpenTokResource
from rest_framework.views import APIView


# Create your views here.
class SessionView(APIView):

    def get(self, request):

        opentok = OpenTokResource.get_client()
        session = opentok.create_session()
        token = opentok.generate_token(session.session_id)
        api_key = settings.APIKEY
        opentok = {'access_token': token,
                   'session_id': session.session_id,
                   'api_key': api_key
                   }
        serializer = OpentokSerializer(data=opentok)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
