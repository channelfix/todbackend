from rest_framework import serializers
from tutors.models import Tutor


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ('user', 'category', 'create_time', 'status')


"""

{"user":1,
"category":[{"id":1},{"id":2}],
"status":0}"""
