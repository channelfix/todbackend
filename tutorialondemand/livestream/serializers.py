from rest_framework import serializers
from livestream.models import Opentok


class OpentokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opentok
        fields = ('access_token', 'session_id', 'api_key')
