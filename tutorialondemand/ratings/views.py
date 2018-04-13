# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
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

        if rate is None:
            raise Http404("No User matches the given query.")

        current_rating = float(data['rating'])
        new_no_of_ratings = rate.no_of_ratings + 1
        new_rating = ((rate.rating * (rate.no_of_ratings)) + current_rating) / (new_no_of_ratings)
        rate.rating = new_rating
        rate.no_of_ratings = new_no_of_ratings
        rate.save(update_fields=['rating', 'no_of_ratings'])
        return Response(True)

    def list(self, request):
        data = request.GET
        rate = Rating.objects.filter(user=data['user']).first()

        if rate is None:
            raise Http404("No User matches the given query.")

        return Response(rate.rating)
