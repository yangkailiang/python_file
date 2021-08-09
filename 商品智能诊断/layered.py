from pywebio import start_server
from pywebio.input import *
from pywebio.output import put_text, put_table, put_buttons, put_markdown
from get_data import *
def input_text():
    index_num = input_group(
        "请输入分层设置",
        [
            input('请输入要查询的店铺ID', name = "shop_id", type=NUMBER),
            input("第一层级访客指数分大于等于：", name="first", type=NUMBER),
            input("第三层级访客量小于：", name="second", type=NUMBER),
            input('优秀，指数分>=', name = 'youxiu', type=NUMBER),
            input('良好，指数分>=', name = 'lianghao', type=NUMBER),
            input('及格，指数分>=', name = 'jige', type=NUMBER),
        ])
    cengji_dict = input_group(
        '请输入指数计算规则',
        [
            input('第一层级访客量占比（百分比）', name='fangke', type=NUMBER),
            input('第一层级加购转化率占比（百分比）', name='jiagou', type=NUMBER),
            input('第一层级点击转化率占比（百分比）', name='dianji', type=NUMBER),
            input('第一层级支付新买家转化率占比（百分比）', name='xinmaijia', type=NUMBER),
            input('第二层级访客量占比（百分比）', name='fangke2', type=NUMBER),
            input('第二层级加购转化率占比（百分比）', name='jiagou2', type=NUMBER),
            input('第二层级点击转化率占比（百分比）', name='dianji2', type=NUMBER),
            input('第二层级支付新买家转化率占比（百分比）', name='xinmaijia2', type=NUMBER),
        ])
    data = get_data(index_num['shop_id'])


    def Deviation(dict,list,key,key_name):
        max_scor = max([i[key] for i in dict])
        # print(key,max_scor)
        min_score = min([i[key] for i in dict])
        # print(key, min_score)
        for i in list:
            values = i[key]
            if max_scor - min_score != 0:
                index_score = (values - min_score) / (max_scor - min_score) * 100
            else:
                index_score = 0
            if index_score >= index_num['youxiu']:
                # i[key_name] = '优秀:%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
                i[key_name] = '优秀:%d'%index_score
            elif index_num['youxiu'] > index_score >= index_num['lianghao']:
                # i[key_name] = '良好%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
                i[key_name] = '良好:%d'%index_score
            elif index_num['lianghao'] > index_score >= index_num['jige']:
                # i[key_name] = '及格%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
                i[key_name] = '及格:%d'%index_score
            else:
                # i[key_name] = '较差%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
                i[key_name] = '较差:%d'%index_score

    max_visitorCount = max([i['visitorCount'] for i in data])
    min_visitorCount = min([i['visitorCount'] for i in data])


    def first(dict):
        list_return = []
        for i in dict:
            values = i['visitorCount']
            index_score = (values-min_visitorCount) / (max_visitorCount-min_visitorCount)*100
            if index_score >= index_num['first']:
                list_return.append(i)
        Deviation(dict, list_return, 'visitorCount', '访客量指数分')
        Deviation(dict, list_return, 'payNewBuyerSum', '支付新买家指数分')
        Deviation(dict, list_return, 'addShoppingRate', '加购率指数分')
        Deviation(dict, list_return, 'clickRate', '点击率指数分')
        Deviation(dict, list_return, 'payNewBuyerRate', '支付新买家转换率指数分')
        return list_return


    def third(list):
        list_return = []
        for i in list:
            if i['visitorCount'] < index_num['second'] and i['productName'] not in [i['productName'] for i in first(list)]:
               list_return.append(i)
        # 获取访客量的离差值
        Deviation(list, list_return,'visitorCount','访客量指数分')
        Deviation(list, list_return, 'payNewBuyerSum', '支付新买家指数分')
        Deviation(list, list_return, 'addShoppingRate', '加购率指数分')
        Deviation(list, list_return, 'clickRate', '点击率指数分')
        Deviation(list, list_return, 'payNewBuyerRate', '支付新买家转换率指数分')
        return list_return


    def second(list):
        list_return = []
        # 获取第二层级的单品
        for i in list:
            if i['productName'] not in [i['productName'] for i in (first(list) + third(list))]:
                list_return.append(i)
        # 计算指数并加入字典
        Deviation(list, list_return, 'visitorCount', '访客量指数分')
        Deviation(list, list_return, 'payNewBuyerSum', '支付新买家指数分')
        Deviation(list, list_return, 'addShoppingRate', '加购率指数分')
        Deviation(list, list_return, 'clickRate', '点击率指数分')
        Deviation(list, list_return, 'payNewBuyerRate', '支付新买家转换率指数分')
        return list_return


    def put_data(data1,text,cengji=0):

        put_text(text)
        list_sum = []
        list_sum2 = []
        list1 = []
        list2 = [['商品名称','访客量','访客量指数分','支付新买家','支付新买家指数分','加购转化率','加购转化率指数分','点击转化率',
                  '点击转化率指数分','支付新买家转换率','支付新买家转换率指数分','单uv','预估同级别交易额','预估同级别支付新买家','关注指数']]
        for i in data1:
            list = []
            list.append(i['productName'])
            list.append(i['visitorCount'])
            list.append(i['访客量指数分'])
            list.append(i['payNewBuyerSum'])
            list.append(i['支付新买家指数分'])
            list.append(i['addShoppingRate'])
            list.append(i['加购率指数分'])
            list.append(i['clickRate'])
            list.append(i['点击率指数分'])
            list.append(i['payNewBuyerRate'])
            list.append(i['支付新买家转换率指数分'])
            if i['payBuyerSum'] > 0:
                list.append(i['payAmount'] / i['payBuyerSum'])
            else:
                list.append(0)
            if i['visitorCount'] > 0:
                list.append(i['payAmount'] * (max_visitorCount / i['visitorCount']))
                list.append(i['payNewBuyerSum'] * (max_visitorCount / i['visitorCount']))
            else:
                list.append(0)
                list.append(0)
            list1.append(list)
            list2.append(list)
        if cengji == 1:
            for i in list1:
                fangkeliang = int(i[2].split(':')[1]) * (cengji_dict['fangke'] / 100)
                jiagou = int(i[6].split(':')[1]) * (cengji_dict['jiagou'] / 100)
                dianji = int(i[8].split(':')[1]) * (cengji_dict['dianji'] / 100)
                zhifu = int(i[10].split(':')[1]) * (cengji_dict['xinmaijia'] / 100)
                sum = fangkeliang + jiagou +dianji + zhifu
                list_sum.append(sum)
            max_sum = max(list_sum)
            for i in list_sum:
                zhishuzhi = i / max_sum
                list_sum2.append(zhishuzhi)
            for items in range(len(list_sum2)):
                list2[items+1].append(list_sum2[items])
        elif cengji == 2:
            for i in list1:
                fangkeliang = int(i[2].split(':')[1]) * (cengji_dict['fangke2'] / 100)
                jiagou = int(i[6].split(':')[1]) * (cengji_dict['jiagou2'] / 100)
                dianji = int(i[8].split(':')[1]) * (cengji_dict['dianji2'] / 100)
                zhifu = int(i[10].split(':')[1]) * (cengji_dict['xinmaijia2'] / 100)
                sum = fangkeliang + jiagou +dianji + zhifu
                list_sum.append(sum)
            max_sum = max(list_sum)
            for i in list_sum:
                zhishuzhi = i / max_sum
                list_sum2.append(zhishuzhi*100)
            for items in range(len(list_sum2)):
                list2[items+1].append(list_sum2[items])

        put_table(list2)



    first_data = first(data)
    third_data = third(data)
    second_data = second(data)
    if first_data != []:
        put_data(first_data, '第一层级,个数为:%d个'%(len(first_data)), 1)
    else:
        put_text('第一层级,个数为0个')
    if second_data != []:
        put_data(second_data, '第二层级,个数为:%d个'%(len(second_data)), 2)
    else:
        put_text('第二层级,个数为0个')
    put_data(third_data, '第三层级,个数为:%d个'%(len(third_data)))

start_server(input_text, port= 7000)