from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('text', 'id')


class CategoryIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',)
