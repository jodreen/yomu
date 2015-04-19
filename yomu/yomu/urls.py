from django.conf.urls import include, url
from django.contrib import admin
from yomu.views import home

urlpatterns = [
    url(r'^$', 'yomu.views.home', name='home_url_name'),
    url(r'^mybooks/$', 'yomu.views.mybooks', name='mybooks_url_name'),
    url(r'^profile/$', 'yomu.views.profile', name='profile_url_name'),
]
