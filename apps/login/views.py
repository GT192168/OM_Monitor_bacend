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


class login(APIView):

    def get(self, request):
        # race_type = request.GET.get('race_type')

        username = request.GET.get('username')
        passwd = request.GET.get('passwd')

        if username == 'admin' and passwd == '123456':
            return Response(ResponseWrapper().execute_success('200'))
        else:
            return Response(ResponseWrapper().mark_custom(False, 500, '密码错误'))



class login1(APIView):

    def get(self, request):
        # race_type = request.GET.get('race_type')
        data_list = ['hello', 'word', '19999']
        data = data_list
        data_a = {
            'data_list': data,
        }
        return Response(ResponseWrapper().execute_success(data=data_a))


def timer(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})


def lg_tim(request):
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d-%H:%M")
    return JsonResponse({'result': 200, 'msg': ctime})
