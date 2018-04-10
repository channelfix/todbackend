from rest_framework import serializers
from requestpool.models import RequestPool


class RequestPoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestPool
        fields = ('id', 'user', 'category', 'status')

    def create(self, validated_data):
        student, created = RequestPool.objects.get_or_create(
            user=validated_data['user'],
            category=validated_data['category'],
            defaults={
                'status': 1,
            })
        return student
