from rest_framework import serializers
from models import Question, Room, RequestAns, Opentok


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RequestAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestAns
        fields = '__all__'


class OpentokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opentok
        fields = '__all__'
