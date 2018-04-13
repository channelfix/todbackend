"""tutorialondemand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from categories import views as category_views
from ratings import views as rating_views
from requestpool import views as request_pool_views
from rooms import views as room_views
from search import views as search_views
from login.views import register_by_access_token


router = routers.DefaultRouter()
router.register(r'category', category_views.CategoryList)
router.register(r'request-pool', request_pool_views.RequestPoolView)
router.register(r'room', room_views.RoomView)
router.register(r'rating', rating_views.RatingView)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^register-by-token/(?P<backend>[^/]+)/$', register_by_access_token),
    url(r'^users/$', search_views.SearchListView.as_view()),
]
