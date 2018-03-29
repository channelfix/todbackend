# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from tutors.models import Tutor
from tutors.serializers import TutorSerializer


# Create your views here.
class TutorView(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    def create(self, request):
        data = request.data
        dataset = []
        for category in data['category']:
            tutor = {'user': data['user'],
                     'category': category,
                     'status': data['status']
                     }
            dataset.append(tutor)
        serializer = TutorSerializer(data=dataset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
