# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets

from users.serializers import UserSerializer
from categories.serializers import CategoryIdSerializer
from random import randint
from requestpool.models import RequestPool
from requestpool.serializers import RequestPoolSerializer


# Create your views here.


class RequestPoolView(viewsets.ModelViewSet):

    queryset = RequestPool.objects.all()
    serializer_class = RequestPoolSerializer

    @detail_route(methods=['get'], url_path='status-to-inactive')
    def status_to_inactive(self, request, pk=None):
        instance = self.get_object()
        serializer = RequestPoolSerializer(instance,
                                           data={'status': 0},
                                           partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-waiting')
    def status_to_waiting(self, request, pk=None):
        instance = self.get_object()
        serializer = RequestPoolSerializer(instance,
                                           data={'status': 1},
                                           partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-pending')
    def status_to_pending(self, request, pk=None):
        instance = self.get_object()
        serializer = RequestPoolSerializer(instance,
                                           data={'status': 2},
                                           partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        user = User.objects.get(id=data['user'])
        serializer = UserSerializer(user, read_only=True)
        data.update({'first_name': serializer.data['first_name'],
                     'last_name': serializer.data['last_name']})
        return Response(data)

    @detail_route(methods=['get'], url_path='status-to-ongoing')
    def status_to_ongoing(self, request, pk=None):
        instance = self.get_object()
        serializer = RequestPoolSerializer(instance,
                                           data={'status': 3},
                                           partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data)


class RetrieveStudent(viewsets.ViewSet):
    queryset = RequestPool.objects.all()

    def list(self, request):
        data = request.GET
        myDict = {}
        for key in data.iterkeys():
            myDict = dict(data.iterlists())
        dataset = []
        for category in myDict['category']:
            dataset.append({'id': category})

        serializer = CategoryIdSerializer(dataset, many=True)
        data = serializer.data

        categories = []
        for category_id in data:
            categories.append(category_id['id'])

        try:
            query = Q(status=1) & Q(category__in=categories)
            student = RequestPool.objects.filter(query)
            count = student.count()
            random_index = randint(0, count - 1)

            serial = RequestPoolSerializer(student[random_index])
            print serial.data

            return Response(serial.data)
        except Exception:
            return Response([])
