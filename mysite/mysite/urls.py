"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 匹配路径，返回后面的视图函数
    path('', views.page_view),
    path('page/', views.page2_view),
    # path转换器
    # int（匹配正整数包括0 ）<int:num>
    # str（匹配除了'/'的字符串）<str:str1>
    # slug （匹配）
    # path （匹配非空字段，包括'/'）<path:all_path>
    path('page/<int:num>', views.page3_view),
    # re_path (正则匹配path)       语法：(?P<name>\d{2})  ?P:固定写法; <name>:定义名字；后面是正则表达式匹配
    re_path(r'^birthday/(?P<year>\d{4})/(?P<mon>\d{2})/(?P<day>\d{2})', views.birthday_view),


    path('page/<int:num1>/<str:str1>/<int:num2>', views.page4_view),
    path('test_html', views.test_html),
    path('test_mycal', views.test_mycal),
    path('test_for', views.test_for)



]
