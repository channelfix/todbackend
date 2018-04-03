# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login

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
    # This view expects an access_token GET parameter, if it's needed,
    # request.backend and request.strategy will be loaded with the current
    # backend and strategy.

    token = request.POST.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        login(request, user)
        return True
    else:
        return False
