# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list, api

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^api/$', api, name='api')
]
