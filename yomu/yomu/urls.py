from django.conf.urls import include, url
from django.contrib import admin
from yomu.views import home

urlpatterns = [
    url(r'^$', 'yomu.views.home', name='home'),

]
