# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q
from tutorialondemand.settings import APIKEY, OPENTOKSECRETKEY
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import viewsets
from opentok import OpenTok
from rooms.models import Room
from rooms.serializers import RoomSerializer
from users.serializers import UserSerializer


# Create your views here.
class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data['id'],
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data['status'])

    @detail_route(methods=['get'], url_path='tutor-token')
    def tutor_token(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance)
        session_id = serializer.data['session_id']
        opentok = OpenTok(APIKEY, OPENTOKSECRETKEY)
        token = opentok.generate_token(session_id)
        data = {'session_id': session_id,
                'APIKEY': APIKEY,
                'token': token}
        return Response(data)

    @detail_route(methods=['get'], url_path='student-token')
    def student_token(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance, data={'status': 2}, partial=True)
        serializer.is_valid()
        serializer.save()
        session_id = serializer.data['session_id']
        opentok = OpenTok(APIKEY, OPENTOKSECRETKEY)
        token = opentok.generate_token(session_id)
        data = {'session_id': session_id,
                'APIKEY': APIKEY,
                'token': token}

        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-inactive')
    def status_to_inactive(self, request, pk=None):
        instance = self.get_object()
        serializer = RoomSerializer(instance,
                                    data={'status': 0},
                                    partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(True)

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

    @list_route(methods=['get'], url_path='retrieve-room')
    def retrieve_room(self, request):
        data = request.GET
        try:
            query = Q(status=1) & Q(user_student=data['user'])
            room = Room.objects.filter(query).first()
            serializer = RoomSerializer(room)
            data = serializer.data
            room_id = data['id']
            user = User.objects.filter(id=data['user_tutor']).first()
            serializer = UserSerializer(user, read_only=True)
            tutor = {}
            tutor.update({'id': room_id,
                          'first_name': serializer.data['first_name'],
                          'last_name': serializer.data['last_name']})
            return Response(tutor)
        except KeyError:
            return Response({})
