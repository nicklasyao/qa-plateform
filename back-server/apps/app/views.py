import json
import logging

from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect

logger = logging.getLogger('log')


# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
        # return redirect('login/')
    return render(request, "index.html")


def logging_in(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_name = body.get('username')
        pass_word = body.get('password')

        user = authenticate(username=user_name, password=pass_word)

        if user is not None:
            auth.login(request, user)
            data = {'name': user.username, 'last_login': user.last_login}
            return JsonResponse(_get_response_json_dic(data))
        else:
            logger.warning('{}登录校验失败，用户名密码不匹配'.format(user_name))
            return JsonResponse(_get_response_json_dic('', -1, u'用户名或密码错误'))
    # get
    return JsonResponse(_get_response_json_dic('', -1, u'无效请求'))


# 封装rest结果
def _get_response_json_dic(data, code=0, message='Success'):
    result_data = {
        'code': code,
        'message': message,
        'data': data
    }
    return result_data


def log_user_out(request):
    auth.logout(request)
    return JsonResponse(_get_response_json_dic('', -1, u'无效请求'))
