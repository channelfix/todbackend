from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from database import views
from .views import SessionView



urlpatterns = [
    url(r'^$', SessionView.as_view(), name ='session')
]