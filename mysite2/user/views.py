from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test_user(request):
    return HttpResponse('这是user页面')
