# -*- coding:utf-8 -*-

from django.conf.urls import url
from .views import tmViews


urlpatterns = [
    # 获取时间信息
    url(r'^tminfo/tm_info$', tmViews.as_view()),

]