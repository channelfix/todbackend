# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse

from social_django.utils import psa
from django.views.decorators.csrf import csrf_exempt

# Define an URL entry to point to this view, call it passing the
# access_token parameter like ?access_token=<token>. The URL entry must
# contain the backend, like this:
#
#   url(r'^register-by-token/(?P<backend>[^/]+)/$',
#       'register_by_access_token')


@csrf_exempt
@psa('social:complete')
def register_by_access_token(request, backend):

    if request.method == 'POST':
        token = request.POST.get('access_token')
        user = request.backend.do_auth(token)

        if user:
            login(request, user)
            user = User.objects.get(username=user).id
            return HttpResponse(user)
        raise Http404("No User matches the given query.")
    raise Http404("GET method was received instead of POST.")
