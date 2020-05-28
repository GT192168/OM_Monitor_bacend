# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import pymysql
from extra_apps.response_wrapper import ResponseWrapper

#

from django.http import JsonResponse
import datetime

def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})

def timer(request):
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d-%H:%M")
    return JsonResponse({'result': 200, 'msg': ctime})