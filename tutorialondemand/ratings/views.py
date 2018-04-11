# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework import viewsets
from ratings.models import Rating
from ratings.serializers import RatingSerializer


# Create your views here.
class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request):
        data = request.data
        rate = Rating.objects.filter(user=data['user']).first()
        rating = rate.rating
        new_no_of_ratings = rate.no_of_ratings + 1
        new_rating = ((rating*(new_no_of_ratings-1))+data['rating']) / (new_no_of_ratings)
        Rating.objects.filter(user=data['user']).update(rating=new_rating, no_of_ratings=new_no_of_ratings)
        return Response(True)

    def list(self, request):
        data = request.GET
        rate = Rating.objects.filter(user=data['user']).first()
        rating = rate.rating
        return Response(rating)
