from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test_login(request):
    return HttpResponse('这是login的页面')