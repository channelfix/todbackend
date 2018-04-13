# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from ratings.models import Rating
from simple_search import search_filter
from social_django.models import UserSocialAuth


class SearchListView(APIView):

    def get(self, request, format=None):
        result = User.objects.all()

        query = self.request.GET.get('q')
        # if query:
        #     x = []
        #     query_list = query.split()
        #     for ctr in query_list:

        #         x.append(result.filter(
        #                 Q(first_name__icontains=ctr) |

        #                 Q(last_name__icontains=ctr)
        #         ))
        #         print x

        search_fields = ['first_name', 'last_name']
        query_list = User.objects.filter(search_filter(search_fields, query))

        result = []
        for user in query_list:
            rating = Rating.objects.filter(user_id=user.id).first()
            avatar = UserSocialAuth.objects.filter(user_id=user.id).first()
            result.append({
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': 'https://avatars.io/facebook/' + avatar.uid,
                'rating': rating.rating
            })

        return Response(result)
