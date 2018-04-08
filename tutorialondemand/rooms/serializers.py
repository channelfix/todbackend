from __future__ import unicode_literals

from tutorialondemand.settings import APIKEY, OPENTOKSECRETKEY
from rest_framework import serializers
from opentok import OpenTok
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'category', 'user_student',
                  'user_tutor', 'session_id', 'status')

    def create(self, validated_data):

        opentok = OpenTok(APIKEY, OPENTOKSECRETKEY)
        session = opentok.create_session()
        session_id = session.session_id
        obj = Room(user_student=validated_data['user_student'],
                   user_tutor=validated_data['user_tutor'],
                   category=validated_data['category'],
                   status=1,
                   session_id=session_id)
        obj.save()
        return obj
