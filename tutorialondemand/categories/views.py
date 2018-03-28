# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import viewsets


# Create your views here.
class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
