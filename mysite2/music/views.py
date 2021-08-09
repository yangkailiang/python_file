from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test_music(request):
    return HttpResponse('这是music的页面')