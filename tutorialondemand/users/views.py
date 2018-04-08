# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from users.serializers import UserSerializer

# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['get'], url_path='get-name')
    def get_name(self, request, pk=None):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        data = "" + serializer.data['first_name'] + " " + serializer.data['last_name']
        return Response(data)
