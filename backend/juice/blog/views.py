import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm


def index(request):
    name = request.GET.get('name')
    print(name or 'World')
    return HttpResponse('Hello, {name}!'.format(name=name or 'World'))


def user_pass(request):
    res = dict()
    res.update({
        'username': 'zhancc',
        'password': '123456'
    })
    return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json, charset=utf-8")
