#!/usr/bin/env python
# -*- coding:utf-8 -*-
from api import views
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^login/',views.LoginView.as_view()),
    url(r'^message/',views.MessageView.as_view())
]