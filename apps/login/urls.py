# -*- coding:utf-8 -*-

from django.urls import path
from . import views
from .views import User

urlpatterns = [
    # 获取时间信息
    path("login", User.as_view(), name='he'),
]