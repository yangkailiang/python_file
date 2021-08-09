import datetime

# from Tools.Generate_log import generate_log


def get_decorator(default_value=''):
    # logger = generate_log().log('/Users/ykl/automated_testin/ES/Data/error.txt')
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                data = func(*args, **kwargs)
                return data
            except Exception as e:
                # logger.error(e)
                return default_value,e
        return new_func
    return decorator
try_except = get_decorator(default_value='报错了')


def sum_up(obj):
    '''
    计算求和
    :param obj: 列表或字典或元组
    :return:和
    '''
    global sum
    if type(obj) == list:
        try:
            sum = sum(obj)
            return sum
        except:
            list1 = []
            for i in obj:
                try:
                    c = int(i)
                    list1.append(c)
                except:
                    return '数据中有其他类型的数据'
            sum = sum(list1)
            return sum
    elif type(obj) == dict:
        list1 = []
        for i in obj.values():
            list1.append(i)
        sum = sum_up(list1)
        return sum
    elif type(obj) == tuple:
        list1 = list(obj)
        sum = sum_up(list1)
        return sum
    else:
        return '该程序暂时只支持 字典、列表和元组'


@try_except
def open_yml(path):
    '''
    打开指定的yaml文件
    :param path: 路径（最好是绝对路径）
    :return: 改文件的所有数据，字典形式返回
    '''
    import yaml
    with open(path,'r',encoding='utf-8') as f:
        return yaml.safe_load(f)


def split_es_date(date):
    '''
    把时间减去8小时，并把格式转换成es的格式
    :param date: 时间  示例：'2012-03-02 00:00:00'
    :return: es格式时间 示例：2012-03-01T16:00:00
    '''
    d1 = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    time = d1 + datetime.timedelta(hours=-8)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S')
    a = str_time.split(' ')
    es_date = a[0] + 'T' + a[1]
    return es_date


def diff_list(list1,list2):
    diff1 = []
    diff2 = []
    list1_diff = set(list1).difference(set(list2))
    list2_diff = set(list2).difference(set(list1))
    if list1_diff == set() and list2_diff == set():
        pass


def division_list(list,num):
    list1 = []
    page = int(len(list) / num) + 1
    for i in range(page):
        list2 = list[i * num : num * (i + 1)]
        if len(list2) != 0:
            list1.append(list2)
        elif len(list2) == 0:
            pass
    return list1


def ergodic_list(fucn, list):
    list_return = []
    for i in list:
        if i == True:
            pass
        else:
            data = fucn(i)
            list_return.append(data)
    return list_return










if __name__ == '__main__':
    # '\n%s中有，但在%s中没有：%s\n%s中有，%s中没有：%s\n' % (name1, name2, dif_list1, name2, name1, dif_list2)
    # list1 = ['1822153860943836901', '1822455651049735810', '1821734570139258613', '1818768710347054154', '1806553332911505063', '1301917659121904387', '1800077727370908156', '1799985531687293648', '1798640931149995254', '1786435344713347874', '1785516120806106842', '1291372536453624876']
    # list2 = ['1291372536453624876', '1822153860943836901', '1799985531687293648', '1818768710347054154', '1776614509006158252', '1786435344713347874', '1798640931149995254', '1780651188459425409', '1821734570139258613', '1301917659121904387', '1785516120806106842', '1806553332911505063', '1800077727370908156']
    # list3 = [1,2]
    # list4 = [1,2,3]
    # a = different_list(list3,list4)
    # print(a{)
    # a = {'a':1}
    # a.update({'b': 1,'a':1})
    # # print(a)
    # a = {}
    #
    # list = []
    # list2 = ['a','b']
    # for i in a.items():
    #     print(i)
    #     if list2 in i:
    #         list.append(i)
    # print(list)
    # a = open_yml('/Users/ykl/automated_testing/ES/Data/url.yaml')
    pass
