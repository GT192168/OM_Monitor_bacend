# -*- coding:utf-8 -*-

from django.urls import path
from . import views
from .views import he

urlpatterns = [
    # 获取时间信息
    path("helloApi", views.hello, name='hello'),  # 第一个参数表示路径
    path("heApi", he.as_view(), name='he'),
    path('ntime', views.timer, name='timer'),

]
