




def Deviation(dict, list, key, key_name, index_num):
    max_scor = max([i[key] for i in dict])
    # print(key,max_scor)
    min_score = min([i[key] for i in dict])
    # print(key, min_score)
    for i in list:
        values = i[key]
        if max_scor - min_score != 0:
            index_score = round(((values - min_score) / (max_scor - min_score) * 100), 3)
        else:
            index_score = 1
        if index_score >= index_num[0]:
            # i[key_name] = '优秀:%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
            i[key_name] = ['a',index_score]
        elif index_num[0] > index_score >= index_num[1]:
            # i[key_name] = '良好%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
            i[key_name] = ['b',index_score]
        elif index_num[1] > index_score >= index_num[2]:
            # i[key_name] = '及格%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
            i[key_name] = ['c',index_score]
        else:
            # i[key_name] = '较差%d,%s除%s'%(index_score,(values - min_score),(max_scor - min_score))
            i[key_name] = ['d',index_score]




def first(dict, first_index, layered):
    max_visitorCount = max([i['visitorCount'] for i in dict])
    min_visitorCount = min([i['visitorCount'] for i in dict])
    list_return = []
    for i in dict:
        values = i['visitorCount']
        index_score = (values - min_visitorCount) / (max_visitorCount -min_visitorCount ) *100
        if index_score >= first_index:
            list_return.append(i)
    Deviation(list_return, list_return, 'visitorCount', '访客量指数分', layered)
    Deviation(list_return, list_return, 'payNewBuyerSum', '支付新买家指数分', layered)
    Deviation(list_return, list_return, 'addShoppingRate', '加购率指数分', layered)
    Deviation(list_return, list_return, 'clickRate', '点击率指数分', layered)
    Deviation(list_return, list_return, 'payNewBuyerRate', '支付新买家转换率指数分', layered)
    return list_return


def third(list, first_index, third_index, layered):
    list_return = []
    for i in list:
        if i['visitorCount'] < third_index and i['productName'] not in [i['productName'] for i in first(list, first_index, layered)]:
            list_return.append(i)
    # 获取访客量的离差值
    Deviation(list_return, list_return ,'visitorCount' ,'访客量指数分', layered)
    Deviation(list_return, list_return, 'payNewBuyerSum', '支付新买家指数分', layered)
    Deviation(list_return, list_return, 'addShoppingRate', '加购率指数分', layered)
    Deviation(list_return, list_return, 'clickRate', '点击率指数分', layered)
    Deviation(list_return, list_return, 'payNewBuyerRate', '支付新买家转换率指数分', layered)
    return list_return


def second(list, first_index, third_index, layered):
    if len(first(list, first_index, layered)) + len(third(list, first_index, third_index, layered)) != len(list):
        list_return = []
        # 获取第二层级的单品
        for i in list:
            if i['productName'] not in [i['productName'] for i in (first(list, first_index, layered) + third(list, first_index, third_index, layered))]:
                list_return.append(i)
        # 计算指数并加入字典
        Deviation(list_return, list_return, 'visitorCount', '访客量指数分', layered)
        Deviation(list_return, list_return, 'payNewBuyerSum', '支付新买家指数分', layered)
        Deviation(list_return, list_return, 'addShoppingRate', '加购率指数分', layered)
        Deviation(list_return, list_return, 'clickRate', '点击率指数分', layered)
        Deviation(list_return, list_return, 'payNewBuyerRate', '支付新买家转换率指数分', layered)
        return list_return
    else:
        return []


def assemble_data(data1, cengji, first_Hierarchy, second_Hierarchy):
    max_visitorCount = max([i['visitorCount'] for i in data1])
    list_sum = []
    list_sum2 = []
    for i in data1:
        if i['payBuyerSum'] > 0:
           i['单uv'] = i['payAmount'] / i['payBuyerSum']
        else:
            i['单uv'] = 0
        if i['visitorCount'] > 0:
            i['预估同级别交易额'] = (i['payAmount'] * (max_visitorCount / i['visitorCount']))
            i['预估同级别支付新买家'] = (i['payNewBuyerSum'] * (max_visitorCount / i['visitorCount']))
        else:
            i['预估同级别交易额'] = 0
            i['预估同级别支付新买家'] = 0
    if cengji == 1:
        for i in data1:
            fangkeliang = i['访客量指数分'][1] * (first_Hierarchy[0] / 100)
            jiagou = i['加购率指数分'][1] * (first_Hierarchy[1] / 100)
            dianji = i['点击率指数分'][1] * (first_Hierarchy[2] / 100)
            zhifu = i['支付新买家转换率指数分'][1] * (first_Hierarchy[3] / 100)
            sum = fangkeliang + jiagou +dianji + zhifu
            list_sum.append(sum)
            print(i['productName'])
            print(i['访客量指数分'][1],fangkeliang)
            print(i['加购率指数分'][1],jiagou)
            print(i['点击率指数分'][1],dianji)
            print(i['支付新买家转换率指数分'][1],zhifu)
            print(sum)
            print('=================')

        max_socre = max(list_sum)
        print(max_socre)
        for i in list_sum:
            guanzhu = i / max_socre
            list_sum2.append(guanzhu)
        for i in range(len(list_sum2)):
            data1[i]['关注指数'] = list_sum2[i] * 100

    elif cengji == 2:
        for i in data1:
            fangkeliang = i['访客量指数分'][1] * (second_Hierarchy[0] / 100)
            jiagou = i['加购率指数分'][1] * (second_Hierarchy[1] / 100)
            dianji = i['点击率指数分'][1] * (second_Hierarchy[2] / 100)
            zhifu = i['支付新买家转换率指数分'][1] * (second_Hierarchy[3] / 100)
            print(i['访客量指数分'][1],fangkeliang,jiagou,dianji,zhifu)
            sum = fangkeliang + jiagou + dianji + zhifu
            list_sum.append(sum)
        max_socre = max(list_sum)
        for i in list_sum:
            guanzhu = i / max_socre
            list_sum2.append(guanzhu)
        for i in range(len(list_sum2)):
            data1[i]['关注指数'] = list_sum2[i] * 100

    return data1



if __name__ == '__main__':
    from get_data import *
    data1 = get_data(3586)
    a = first(data1,20, [80, 57, 30])
    b = assemble_data(a, 1, [20,20,20,40], [20,20,20,40])
    print(b)
    # for i in b:
    #     print(i)