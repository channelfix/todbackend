# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from social_django.models import UserSocialAuth
from social_django.utils import psa

from ratings.models import Rating
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Define an URL entry to point to this view, call it passing the
# access_token parameter like ?access_token=<token>. The URL entry must
# contain the backend, like this:
#
#   url(r'^register-by-token/(?P<backend>[^/]+)/$',
#       'register_by_access_token')


@api_view(['GET', 'POST', ])
@csrf_exempt
@psa('social:complete')
def register_by_access_token(request, backend):

    if request.method == 'POST':
        token = request.POST.get('access_token')
        user = request.backend.do_auth(token)

        if user:
            login(request, user)
            user = User.objects.filter(username=user).first()
            user_id = user.id
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            avatar = UserSocialAuth.objects.filter(user_id=user_id).first().uid
            rating, created = Rating.objects.get_or_create(
                user=user,
                defaults={
                    'rating': 0,
                    'no_of_ratings': 0
                })

            profile = {'user_id': user_id,
                       'first_name': first_name,
                       'last_name': last_name,
                       'email': email,
                       'avatar': 'https://avatars.io/facebook/' + avatar,
                       'rating': rating.rating
                       }
            print profile
            return Response(profile)
        raise Http404("No User matches the given query.")
    raise Http404("GET method was received instead of POST.")
