from time import ctime

from Get_data.get_es_data import get_es_data
from Tools.tools import *


@try_except
def get_shop_id_list(fucn):
    def shop_service(*args,**kwargs ):
        data = fucn(*args,**kwargs)
        list = []
        list.append([i['id'] for i in data['data']['data']['list']])
        list.append([i['shopName'] for i in data['data']['data']['list']])
        return list
    return shop_service
@try_except
def get_zhanbao_data_list(fucn):
    def zhabao_shop(*args,**kwargs):
        data = fucn(*args,**kwargs)
        dict = {}
        if data['data']['code'] == '20000':
            dict['net_sale'] = '搜索店铺数据不在权限范围内！'
            dict['sales'] = '搜索店铺数据不在权限范围内！'
            return dict
        elif data['data']['code'] == '10000':
            list1 = data['data']['data']['list'][0]
            dict['net_sale']=list1['newCusSale']
            dict['sales'] = list1['sales']
            return dict
        else:
            dict['net_sale'] = '未知原因'
            dict['sales'] = '未知原因'
            return dict
    return zhabao_shop
@try_except
def get_zhanbao_department_data(fucn):
    def zhanbao_bumen(*args,**kwargs):
        dict = {}
        data = fucn(*args,**kwargs)
        c = data['data']['data']['departmentReport']
        x_name = [i['name'] for i in c]
        dict['销售额']=[i['sales'] for i in c]
        dict['可提佣销售额'] = [i['achive'] for i in c]
        return x_name,dict
    return zhanbao_bumen
@try_except
def get_zhanbao_bill_data(shop_id,staues):
    from Get_data.get_yunying_data import Zhanbao_api
    bill =Zhanbao_api().bill_sale(shop_id,staues,1)
    page = int(bill['data']['data']['total']/500)+1
    dict = {}
    for i in range(1,page+1):
        bill_two = Zhanbao_api().bill_sale(shop_id,staues,i)
        data1 = bill_two['data']['data']['list']
        for i in data1:
            dict[i['orderId']] = i['sales']
    return dict


if __name__ == '__main__':
    # starttime = "2021-05-01 00:00:00"
    # endtime = "2021-05-31 23:59:59"
    # a ,b, c= get_es_data('1264',starttime,endtime)
    for i in range(10):
        print(ctime())
        bill = get_zhanbao_bill_data(10763,'1')
        print(list(bill.values()))
        print(ctime())
        print('--------------------------------------------------------------')
    # aaa = dict( c, **c )
    # print(len(aaa))
    # for i in aaa:
    #     print(i)

