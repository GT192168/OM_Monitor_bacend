# -*- coding:utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from extra_apps.response_wrapper import ResponseWrapper


class User(APIView):
    # 测试数据
    tokens = {
        'admin': {
            'token': 'admin-token'
        },
        'editor': {
            'token': 'editor-token'
        }
    }
    # 测试数据
    users = {
        'admin-token': {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin'
        },
        'editor-token': {
            'roles': ['editor'],
            'introduction': 'I am an editor',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Normal Editor'
        }
    }

    def post(self, request):
        """
        登录
        @param request: 用户名 密码
        @return: 登录成功返回token
        """
        username = request.data.get('username')
        # password = request.data.get('password') 测试数据先不校验密码
        token = User.tokens.get(username, 0)
        if token:
            return Response(ResponseWrapper().execute_success(token))
        else:
            return Response(ResponseWrapper().mark_custom(False, 500, 'Account and password are incorrect.'))

    def get(self, request):
        """
        获取用户信息
        @param request: token
        @return: 用户头像，简介，用户名，用户权限
        """
        token = request.GET.get('token')
        data = User.users.get(token, 0)
        if data:
            return Response(ResponseWrapper().execute_success(data=data))
        else:
            return Response(ResponseWrapper().mark_custom(False, 500, 'token error'))

    def delete(self, request):
        """
        用户退出登录，删除请求头中对应的token
        @param request
        @return:
        """
        # TODO 删除服务器与请求头中对应的token
        return Response(ResponseWrapper().execute_success())