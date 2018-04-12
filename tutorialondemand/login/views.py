# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from social_django.models import UserSocialAuth
from social_django.utils import psa

from ratings.models import Rating
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@csrf_exempt
@psa('social:complete')
def register_by_access_token(request, backend):

    if request.method == 'GET':
        raise Http404("GET method was received instead of POST.")
    token = request.POST.get('access_token')
    user = request.backend.do_auth(token)

    if user is None:
        raise Http404("No User matches the given query.")

    login(request, user)
    user = User.objects.filter(username=user).first()
    avatar = UserSocialAuth.objects.filter(user_id=user.id).first().uid
    rating, created = Rating.objects.get_or_create(
        user=user,
        defaults={
            'rating': 0,
            'no_of_ratings': 0
        })

    profile = {'user_id': user.id,
               'first_name': user.first_name,
               'last_name': user.last_name,
               'email': user.email,
               'avatar': 'https://avatars.io/facebook/' + avatar,
               'rating': rating.rating,
               'date_joined': user.date_joined
               }
    return Response(profile)
