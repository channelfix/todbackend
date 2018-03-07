from django.conf.urls import url
from database.views import SessionView


urlpatterns = [
    url(r'^$', SessionView.as_view(), name='session')
]