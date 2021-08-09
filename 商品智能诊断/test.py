import pytest
from layered_test import *
from get_data import get_data
import pytest_check
class Test():
    saas_data = get_data(1219)
    layered = [80,60,40]
    first_index = [10,10,10,70]         # [25,25,25,25]     [10,10,10,70]
    second_index = [10,10,10,70]            # [25,25,25,25]
    saas_first = []
    saas_second = []
    saas_third = []
    first_data = first(saas_data, 20, layered)
    third_data = third(saas_data, 20, 100, layered)

    second_data = second(saas_data, 20, 100, layered)
    assemble_first_data = assemble_data(first_data, 1, first_index, second_index)
    if second_data != []:
        assemble_second_data = assemble_data(second_data, 2, first_index, second_index)
    else:
        assemble_second_data = []
    assemble_third_data = assemble_data(third_data, 3, first_index, second_index)
    def test_index(self):
        for i in self.saas_data:
            if i['levelNum'] == 1:
                self.saas_first.append(i)
            elif i['levelNum'] == 2:
                self.saas_second.append(i)
            else:
                self.saas_third.append(i)
        first_saas_diff = set([i['productName'] for i in self.first_data]).difference(set([i['productName'] for i in self.assemble_first_data]))
        first_me_diff = set([i['productName'] for i in self.assemble_first_data]).difference(set([i['productName'] for i in self.first_data]))
        second_saas_diff = set([i['productName'] for i in self.second_data]).difference(set([i['productName'] for i in self.assemble_second_data]))
        second_me_diff = set([i['productName'] for i in self.assemble_second_data]).difference(set([i['productName'] for i in self.second_data]))
        third_saas_diff = set([i['productName'] for i in self.third_data]).difference(set([i['productName'] for i in self.assemble_third_data]))
        third_me_diff = set([i['productName'] for i in self.assemble_third_data]).difference(set([i['productName'] for i in self.third_data]))
        # 断言 分层是否正确
        pytest_check.equal(first_saas_diff, first_me_diff, print(first_saas_diff, first_me_diff))
        pytest_check.equal(second_saas_diff,second_me_diff, print(second_saas_diff, second_me_diff))
        pytest_check.equal(third_saas_diff, third_me_diff, print(third_saas_diff,third_me_diff))

    def test_first_biaoxian(self):
        print('优秀指数分大于等：%d\n良好指数分大于等于：%d\n及格指数分大于等于：%d\n'%(self.layered[0], self.layered[1], self.layered[2]))
        print('第一层级访客量占比（百分比）：%d\n第一层级加购转化率占比（百分比）:%d\n第一层级点击转化率占比（百分比）:%d\n第一层级支付新买家转化率占比（百分比）:%d\n'%(self.first_index[0],self.first_index[1],self.first_index[2],self.first_index[3]))
        print('第一层级访客量占比（百分比）：%d\n第一层级加购转化率占比（百分比）:%d\n第一层级点击转化率占比（百分比）:%d\n第一层级支付新买家转化率占比（百分比）:%d\n'%(self.second_index[0],self.second_index[1],self.second_index[2],self.second_index[3]))
        for num in range(len(self.first_data)):
            saas_data = self.first_data[num]
            me_data = self.assemble_first_data[num]
            shop_name = saas_data['productName']
            print(shop_name)
            pytest_check.equal(saas_data['visitorCountFactor'], me_data['访客量指数分'][0], print('%s(saas//计算):%s,%s'%('访客量指数分', saas_data['visitorCountFactor'], me_data['访客量指数分'][0])))
            pytest_check.equal(saas_data['addShoppingRateFactor'], me_data['加购率指数分'][0], print('%s(saas//计算):%s,%s'%('加购率指数分', saas_data['addShoppingRateFactor'], me_data['加购率指数分'][0])))
            pytest_check.equal(saas_data['clickRateFactor'], me_data['点击率指数分'][0], print('%s(saas//计算):%s,%s'%('点击率指数分', saas_data['clickRateFactor'], me_data['点击率指数分'][0])))
            pytest_check.equal(saas_data['payNewBuyerSumFactor'], me_data['支付新买家指数分'][0], print('%s(saas//计算):%s,%s'%('支付新买家指数分', saas_data['payNewBuyerSumFactor'], me_data['支付新买家指数分'][0])))
            pytest_check.equal(saas_data['payNewBuyerRateFactor'], me_data['支付新买家转换率指数分'][0], print('%s(saas//计算):%s,%s'%('支付新买家转换率指数分', saas_data['payNewBuyerRateFactor'], me_data['支付新买家转换率指数分'][0])))
            pytest_check.equal(int(saas_data['popularRate']), int(me_data['关注指数']), print('%s(saas//计算):%s,%s'%('关注指数', saas_data['popularRate'], round(me_data['关注指数'], 3))))
            print('=================================================================>')

    def test_second_biaoxian(self):
        if self.second_data != []:
            print('优秀指数分大于等：%d\n良好指数分大于等于：%d\n及格指数分大于等于：%d\n' % (self.layered[0], self.layered[1], self.layered[2]))
            print('第一层级访客量占比（百分比）：%d\n第一层级加购转化率占比（百分比）:%d\n第一层级点击转化率占比（百分比）:%d\n第一层级支付新买家转化率占比（百分比）:%d\n' % (
            self.first_index[0], self.first_index[1], self.first_index[2], self.first_index[3]))
            print('第一层级访客量占比（百分比）：%d\n第一层级加购转化率占比（百分比）:%d\n第一层级点击转化率占比（百分比）:%d\n第一层级支付新买家转化率占比（百分比）:%d\n' % (
            self.second_index[0], self.second_index[1], self.second_index[2], self.second_index[3]))
            for num in range(len(self.second_data)):
                saas_data = self.second_data[num]
                me_data = self.assemble_second_data[num]
                shop_name = saas_data['productName']
                print(shop_name)
                pytest_check.equal(saas_data['visitorCountFactor'], me_data['访客量指数分'][0], print('%s(saas//计算):%s,%s'%('访客量指数分', saas_data['visitorCountFactor'], me_data['访客量指数分'][0])))
                pytest_check.equal(saas_data['addShoppingRateFactor'], me_data['加购率指数分'][0], print('%s(saas//计算):%s,%s'%('加购率指数分', saas_data['addShoppingRateFactor'], me_data['加购率指数分'][0])))
                pytest_check.equal(saas_data['clickRateFactor'], me_data['点击率指数分'][0], print('%s(saas//计算):%s,%s'%('点击率指数分', saas_data['clickRateFactor'], me_data['点击率指数分'][0])))
                pytest_check.equal(saas_data['payNewBuyerSumFactor'], me_data['支付新买家指数分'][0], print('%s(saas//计算):%s,%s'%('支付新买家指数分', saas_data['payNewBuyerSumFactor'], me_data['支付新买家指数分'][0])))
                pytest_check.equal(saas_data['payNewBuyerRateFactor'], me_data['支付新买家转换率指数分'][0], print('%s(saas//计算):%s,%s'%('支付新买家转换率指数分', saas_data['payNewBuyerRateFactor'], me_data['支付新买家转换率指数分'][0])))
                pytest_check.equal(int(saas_data['popularRate']), int(me_data['关注指数']), print('%s(saas//计算):%s,%s'%('关注指数', saas_data['popularRate'], round(me_data['关注指数'], 3))))
                print('=================================================================>')
        else:
            print('第二层级没有')

