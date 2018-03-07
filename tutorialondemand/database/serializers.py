from rest_framework import serializers
from database.models import Question, Room, RequestAnswer, Opentok


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('user', 'status', 'text')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('student', ' tutor', 'question', 'session_id', 'timestamp')


class RequestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestAnswer
        fields = ('owner', 'question', 'status')


class OpentokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opentok
        fields = ('access_token', 'session_id', 'api_key')
