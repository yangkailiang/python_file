from django.http import HttpResponse
from django.shortcuts import render


def page_view(request):
    return HttpResponse('这是我设置的空页面')


def page2_view(request):
    return HttpResponse('这是我设置的添加path后的页面')


def page3_view(request, num):
    return HttpResponse('这是我练习path转换器，生成的第%s个网页'%num)


def page4_view(request, num1, str1, num2):
    if str1 not in ['add', 'jian', 'cheng']:
        return HttpResponse('超出范围')
    result = 0
    if str1 == 'add':
        result = num1 + num2
    elif str1 == 'jian':
        result = num1 - num2
    elif str1 == 'cheng':
        result = num1 * num2
    return HttpResponse('这是我练习path转换器组合生成的计算结果%s'%result)


def birthday_view(request, year, mon, day):
    return HttpResponse('这是我练习re_path正则匹配path生成的生日%s-%s-%s' % (year, mon, day))


def get_post_data(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return HttpResponse('这是我练习判断请求是get or post ，以及获取get and post 方法里的数据')


def test_html(request):
    # 引入render模块   from django.shortcuts import render
    # 创建模版层后用render方法来传递模版层的文件（request, '模版层文件', 字典）
    # 字典的取值（在模版层调用传递的参数，必须为字典类型）
    # 字符串 ： 在模版层中{{ key值 }} 调用
    # int ：同上
    # 列表 ：取列表内的某一个值 {{ 列表.index }}调用；例如：{{ list.0 }} 取列表内的第一个元素
    # 函数 ：{{ 函数名 }} 直接调用，注意函数名后面不能加()
    # 类对象 ：
    dic = {}
    dic['name'] = 'yangkailiang'
    dic['int'] = 100
    dic['list'] = [1, 3, 4, 5, 6]

    return render(request, 'test_html.html', dic)


def test_mycal(request):
    # 练习生成一个简单的计算器
    # 模版层调用变量时，如果没有传，不会报错
    # 回显列表 selected

    if request.method == 'GET':
        return render(request, 'mycal.html')

    elif request.method == 'POST':
        op = request.POST['op']
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        result = 0
        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            result = num1 / num2

        return render(request, 'mycal.html', locals())


def test_for(request):
    # 练习for标签
    lst = ['yyy', 'kkk', 'ccc']
    return render(request, 'test_for.html', locals())

















