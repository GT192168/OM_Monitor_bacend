# -*- coding:utf-8 -*-

from django.urls import path
from . import views
from .views import login1
from .views import login

urlpatterns = [
    # 获取时间信息
    path("login_tim", views.lg_tim, name='hello'),  # 第一个参数表示路径
    path("login", login.as_view(), name='he'),
    path("login1", login1.as_view(), name='he1'),
    path('ntime', views.timer, name='timer'),

]