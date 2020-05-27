# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import pymysql
from extra_apps.response_wrapper import ResponseWrapper

#
#
class tmViews(APIView):

    def get(self, request):

        pass

