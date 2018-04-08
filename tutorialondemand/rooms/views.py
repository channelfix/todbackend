# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tutorialondemand.settings import APIKEY, OPENTOKSECRETKEY
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from opentok import OpenTok
from rooms.models import Room
from rooms.serializers import RoomSerializer


# Create your views here.
class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @detail_route(methods=['get'], url_path='create-token')
    def create_token(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance)
        session_id = serializer.data['session_id']
        opentok = OpenTok(APIKEY, OPENTOKSECRETKEY)
        token = opentok.generate_token(session_id)
        return Response(token)

    @detail_route(methods=['get'], url_path='status-to-inactive')
    def status_to_inactive(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance,
                                    data={'status': 0},
                                    partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-waiting')
    def status_to_waiting(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance,
                                    data={'status': 1},
                                    partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-ongoing')
    def status_to_ongoing(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance,
                                    data={'status': 2},
                                    partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)
