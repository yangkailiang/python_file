from time import ctime

import pytest
import pytest_check
import allure


from Get_data.get_yunying_data import Zhanbao_api
from Get_data.get_myaql_data import *
from Ornament.ornament_yunying import *
from Tools.thresding import MyThread

@allure.feature('账单核验')
class Test_chect():
    shop_id = Zhanbao_api().shop_service('2',20)
    @allure.story('核验净销售额、订单个数以及差异订单')
    @allure.severity('critical')
    @allure.description('获取数据库内的账单数据，和es查询到的数据做对比')
    @allure.step('店铺ID')
    # @pytest.mark.parametrize('shop_id',[1279] )
    # @pytest.mark.P0
    @pytest.mark.parametrize('shop_id', shop_id[0], ids= shop_id[1])
    def test_bill_sale(self, shop_id):
        # print('\n程序开始：%s'%ctime())
        starttime = "2021-07-01 00:00:00"
        endtime = "2021-07-30 23:59:59"
        res1 = bill_mysql_data(shop_id, '2021-07')
        # print('\n获取数据库billid：%s' % ctime())
        t2 = MyThread(get_zhanbao_bill_data, (res1[0], '1'))
        t3 = MyThread(get_es_data, (shop_id, starttime, endtime))
        t2.start()
        t3.start()
        t2.join()
        t3.join()                           # 从数据库获取该店铺指定月份的  billid和 可提佣销售额、补差额金额、有效订单个数
        res2 = t2.get_result()                                   # 从运营后台获取该billid的 订单个数、可提佣销售额（列表）、订单id
        res3 = t3.get_result()                                   # 从es获取该店铺指定时间内的 订单id、可提佣销售额（列表）
        # print('\n获取后台和es数据：%s' % ctime())
        '''获取校验字段'''
        '''获取es、账单的新客户销售额列表'''
        es_list_net_sale = list(res3.values())
        yunying_list_net_sale = list(res2.values())
        '''计算es、账单、mysql的新客户销售额之和'''
        es_sum_net_sale = round(sum(es_list_net_sale), 2)
        yunying_sum_net_sale = round(sum(yunying_list_net_sale), 2)
        mysql_sum_net_sale = float(round(res1[1], 2))
        '''获取es、账单的订单列表'''
        old_es_order = list(res3.keys())
        es_order = []
        buchae = {}
        yunying_order = list(res2.keys())
        for i in old_es_order:
            if len(i) == 16:
                buchae[i] = es_list_net_sale[old_es_order.index(i)]
            else:
                es_order.append(i)


        dict_bill = {}
        dict_es = {}
        '''获取列表差值'''
        # print('\n对数据做处理：%s'%ctime())
        yunying_diff = set(es_order).difference(set(yunying_order))
        es_diff = set(yunying_order).difference(set(es_order))
        if yunying_diff == set() and es_diff == set():
            dict_bill[True] = True
            dict_es[True] = True
        elif yunying_diff != set() and es_diff == set():
            for i in yunying_diff:
                dict_bill[i] = es_list_net_sale[es_order.index(i)]
        elif es_diff != set() and yunying_diff == set():
            for i in es_diff:
                dict_es[i] = yunying_list_net_sale[yunying_order.index(i)]
        elif yunying_diff != set() and es_diff != set():
            for i in yunying_diff:
                dict_bill[i] = es_list_net_sale[es_order.index(i)]
            for i in es_diff:
                dict_es[i] = yunying_list_net_sale[yunying_order.index(i)]
        else:
            dict_es['报错了'] = '报错了'
            dict_bill['报错了'] = '报错了'
        # print('\n对比不同：%s'%ctime())
        t4 = MyThread(bill_mysql_refund, (es_order,))
        t4.start()
        t5 = MyThread(ergodic_list, (bill_order_info, dict_bill.keys()))
        t5.start()
        t4.join()
        t5.join()
        mysql_sales = t4.get_result()
        order_info_list = t5.get_result()
        # print('\n获取数据库退单信息：%s' % ctime())
        str1 = '---------------------------------------------------------------'
        print('查询时间范围%s---%s' % (starttime, endtime))

        pytest_check.equal(mysql_sum_net_sale, round((es_sum_net_sale - mysql_sales), 2), print(
            '%s\nbill_id:%s\n数据库中的可提佣销售额（包含补差额）:%s\n账单中计算的总和（累加和不包括补差额）:%s\nes中的可提佣销售额(包含补差额):%s-%s=%s' % (
            str1, res1[0],mysql_sum_net_sale,yunying_sum_net_sale, es_sum_net_sale,mysql_sales,round((es_sum_net_sale - mysql_sales), 2))))
        pytest_check.equal(len(yunying_order), len(es_order), print(
            '%s\n账单中订单个数:%d\nes中的订单个数：%d\n数据库中的有效订单个数：%d\n补差额订单：%s\n' % (str1, len(yunying_order), len(es_order), res1[3], buchae)))
        pytest_check.equal(yunying_diff, es_diff, print(
            '%s\n运营后台账单中有，es中没有：%s\n%s\nes中有运营后台账单中没有：%s\n查询数据库的订单状态:%s' % (
            str1, dict_es, str1, dict_bill,  order_info_list)))
        # print('\n判断结束：%s' % ctime())
